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
import json
import logging
import urllib
import urlparse
import sys

try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request

import killbill

logger = logging.getLogger('killbill')


class Resource(object):
    KILLBILL_API_PREFIX = '/1.0/kb'

    def __init__(self, d):
        for key, value in d.items():
            setattr(self, key, value)

    def __repr__(self):
        return '%s %s' % (self.__class__, self.to_json)

    def build_options(self, **options):
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
        return json.dumps(self, default=lambda o: o.__dict__)

    def refresh(self, raw_response, **options):
        url = raw_response['response'].headers['Location']
        raw_get_response = self.get(url, self.build_options(**options))
        return self.__class__.fromJson(raw_get_response['body'])

    @classmethod
    def fromJson(cls, jsonString):
        return json.loads(jsonString, object_hook=cls.dict_to_object)

    @classmethod
    def dict_to_object(cls, d):
        return cls(**d)

    @classmethod
    def get(cls, relative_uri, options):
        options['method'] = 'GET'
        return cls.send_request(relative_uri, options)

    @classmethod
    def post(cls, relative_uri, body, options):
        options['method'] = 'POST'
        options['body'] = body
        return cls.send_request(relative_uri, options)

    @classmethod
    def send_request(cls, relative_uri, options):
        headers = {}
        options = {k: v for k, v in options.items() if v}

        if 'user' in options:
            headers['X-Killbill-CreatedBy'] = options['user']

        if 'reason' in options:
            headers['X-Killbill-Reason'] = options['reason']

        if 'comment' in options:
            headers['X-Killbill-Comment'] = options['comment']

        if 'username' in options:
            base64string = base64.b64encode('%s:%s' % (options['username'], options['password']))
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

        uri = urlparse.urlparse(relative_uri)
        # Need to encode in case of spaces (e.g. /1.0/kb/security/users/Mad Max/roles)
        uri = uri._replace(path=urllib.quote(uri.path))
        if uri.scheme == '' and 'baseUri' in options:
            base_uri = urlparse.urlparse(options['baseUri'])
            uri = uri._replace(scheme=base_uri.scheme, netloc="{}:{}".format(base_uri.hostname, base_uri.port))

        url = uri.geturl()
        logger.info("Request method='%s', url='%s'", options['method'], url)
        if 'body' in options:
            logger.debug("Request body='%s'", options['body'])
            request = Request(url, data=options['body'], headers=headers)
        else:
            request = Request(url, headers=headers)

        request.get_method = lambda: options['method']
        response = urlopen(request)
        response_body = response.read()
        logger.debug("Response body='%s'", response_body)
        return {'response': response, 'body': response_body}
