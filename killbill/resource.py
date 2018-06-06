#
# Copyright 2011-2014 Ning, Inc.
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#
import base64
import logging
import sys

import re

try:
    # For Python 3.0 and later
    from urllib.request import build_opener, urlopen, Request, HTTPError
    from urllib.parse import urlencode, urlparse, urlunparse, quote
except ImportError:
    from urllib import quote, urlencode
    from urllib2 import build_opener, urlopen, Request, BaseHandler, HTTPError
    from urlparse import urlparse, urlunparse

import killbill

logger = logging.getLogger('killbill')


class Resource(object):
    KILLBILL_API_PREFIX = '/1.0/kb'

    PERF_REGEXP = re.compile('(/1.0/kb(?:/\w+){1,2}/)\w+-\w+-\w+-\w+-\w+(/\w+)*')

    def __init__(self, d):
        for key, value in d.items():
            setattr(self, key, value)

    def __repr__(self):
        return '%s %s' % (self.__class__, self.to_json())

    @staticmethod
    def build_options(**options):
        default = {
            'contentType': 'application/json',
            'baseUri': killbill.base_uri,
            'username': killbill.username,
            'password': killbill.password,
            'apiKey': killbill.api_key,
            'apiSecret': killbill.api_secret
        }
        default.update(options)
        return default

    def to_json(self):
        return killbill.json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def get_refresh_query(cls):
        return {}

    def refresh(self, raw_response, **options):
        url = raw_response['response'].headers['Location']
        return self.get(url, self.get_refresh_query(), self.build_options(**options))

    @classmethod
    def fromJson(cls, jsonString):
        return killbill.json.loads(jsonString, object_hook=cls.dict_to_object)

    @classmethod
    def dict_to_object(cls, d):
        return cls(**d)

    @classmethod
    def get(cls, relative_uri, query_params, options):
        options['method'] = 'GET'
        options['queryParams'] = query_params
        raw_get_response = cls.send_request(relative_uri, options)
        return cls.fromJson(raw_get_response['body'])

    @classmethod
    def post(cls, relative_uri, body, query_params, options):
        options['method'] = 'POST'
        options['body'] = body
        options['queryParams'] = query_params
        return cls.send_request(relative_uri, options)

    @classmethod
    def delete(cls, relative_uri, body, query_params, options):
        options['method'] = 'DELETE'
        options['body'] = body
        options['queryParams'] = query_params
        return cls.send_request(relative_uri, options)

    @classmethod
    def put(cls, relative_uri, body, query_params, options):
        options['method'] = 'PUT'
        options['body'] = body
        options['queryParams'] = query_params
        return cls.send_request(relative_uri, options)

    @classmethod
    def send_request(cls, relative_uri, options):
        headers = {}
        options = dict((k, v) for k, v in options.items() if v is not None)

        if 'user' in options:
            headers['X-Killbill-CreatedBy'] = options['user']

        if 'reason' in options:
            headers['X-Killbill-Reason'] = options['reason']

        if 'comment' in options:
            headers['X-Killbill-Comment'] = options['comment']

        if 'username' in options:
            base64string = base64.b64encode(
                ('%s:%s' % (options['username'], options['password'])).encode("utf-8")).decode("utf-8")
            headers['Authorization'] = "Basic %s" % base64string

        if 'apiKey' in options:
            headers['X-Killbill-ApiKey'] = options['apiKey']

        if 'apiSecret' in options:
            headers['X-Killbill-ApiSecret'] = options['apiSecret']

        if 'sessionId' in options:
            headers['Cookie'] = 'JSESSIONID=' + options['sessionId']

        if 'requestId' in options:
            headers['X-Request-Id'] = options['requestId']

        if 'accept' in options:
            headers['Accept'] = options['accept']

        if 'contentType' in options:
            headers['Content-Type'] = options['contentType']

        headers['User-Agent'] = 'killbill/v1; Python %s' % (".".join(map(str, sys.version_info)))

        #
        # Extract profiling data map if it exists and set X-Killbill-Profiling-Req HTTP header
        # (there will be no synchronization done, so if multiple threads are running they should probably
        # pass a per-tread profiling Map)
        #
        cur_thread_profiling_data = None
        if 'profilingData' in options:
            headers['X-Killbill-Profiling-Req'] = 'JAXRS'
            cur_thread_profiling_data = options['profilingData']

        uri = urlparse(relative_uri)
        # Need to encode in case of spaces (e.g. /1.0/kb/security/users/Mad Max/roles)
        new_path = quote(uri.path)
        if uri.scheme == '' and 'baseUri' in options:
            base_uri = urlparse(options['baseUri'])
            new_scheme = base_uri.scheme
            new_netloc = "%s:%s" % (base_uri.hostname, base_uri.port)
        else:
            new_scheme = uri.scheme
            new_netloc = uri.netloc

        if 'queryParams' in options:
            new_query_params = urlencode(options['queryParams'])
        else:
            new_query_params = uri.params

        url = urlunparse((new_scheme, new_netloc, new_path, '', new_query_params, ''))
        logger.info("Request method='%s', url='%s', headers='%s'", options['method'], url, headers)
        if 'body' in options:
            body = options['body'].encode("utf-8")
            logger.debug("Request body='%s'", body)
            request = Request(url, data=body, headers=headers)
        else:
            request = Request(url, headers=headers)

        request.get_method = lambda: options['method']

        if killbill.opener:
            opener = build_opener(killbill.opener)
        else:
            opener = build_opener()

        try:
            response = opener.open(request)
        except HTTPError:
            _, err, _ = sys.exc_info()
            # Python 2.5 support
            if not (200 <= err.code < 300):
                raise err
            else:
                response = err.fp

        # Add profiling data if required
        if cur_thread_profiling_data is not None and 'X-Killbill-Profiling-Resp' in response.headers:
            profiling_header = killbill.json.loads(response.headers['X-Killbill-Profiling-Resp'])
            jaxrs_profiling_header = profiling_header['rawData'][0]

            m = Resource.PERF_REGEXP.search(new_path)
            if m:
                second_arg = m.group(2)
                if second_arg is None:
                    second_arg = ''
                key = "%s:%suuid%s" % (options['method'], m.group(1), second_arg)
            else:
                key = "%s:%s" % (options['method'], new_path)

            if not key in cur_thread_profiling_data:
                cur_thread_profiling_data[key] = []

            cur_thread_profiling_data[key].append(jaxrs_profiling_header['durationUsec'])

        response_body = response.read()
        logger.debug("Response body='%s'", response_body)
        return {'response': response, 'body': response_body}
