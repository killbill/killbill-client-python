#
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
try:
    # For Python 3.0 and later
    from urllib.request import HTTPHandler
except ImportError:
    from urllib2 import HTTPHandler

from net.grinder.plugin.http import HTTPRequest
from HTTPClient import NVPair


class GrinderHTTPHandler(HTTPHandler):
    class GrinderHTTPResponse(object):
        def __init__(self, gresp):
            self.gresp = gresp
            self.data = gresp.getText()
            self.code = gresp.getStatusCode()
            self.msg = gresp.getReasonLine()
            self.headers = {}
            for item in gresp.listHeaders():
                self.headers[item] = gresp.getHeader(item)

        def info(self):
            return self.headers

        def read(self):
            return self.data

        def readline(self):
            self.read()

    def http_open(self, req):
        greq = HTTPRequest()

        url = req.get_full_url()
        payload = req.get_data()
        headers = []
        for k, v in req.headers.items():
            headers.append(NVPair(k, v))

        if req.get_method() == 'GET':
            gresp = greq.GET(url, payload, headers)
        elif req.get_method() == 'POST':
            gresp = greq.POST(url, payload, headers)
        elif req.get_method() == 'PUT':
            gresp = greq.PUT(url, payload, headers)
        elif req.get_method() == 'DELETE':
            gresp = greq.DELETE(url, payload, headers)
        else:
            raise ValueError("HTTP method " + req.get_method() + " isn't supported")

        return self.GrinderHTTPResponse(gresp)
