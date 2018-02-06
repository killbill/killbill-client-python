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

user = 'KillBill Python Client'
base_uri = 'http://localhost:8080'
username = 'admin'
password = 'password'
api_key = 'bob'
api_secret = 'lazar'

try:
    import json
except ImportError:
    # Python 2.5 compatibility (import your own json module, e.g. killbill.json=simplejson)
    pass

# Custom urllib opener, e.g.:
#   from killbill.grinder_http_handler import GrinderHTTPHandler
#   killbill.opener = GrinderHTTPHandler
opener = None

import logging

logging.basicConfig(level=logging.DEBUG)

from killbill.resource import Resource
from killbill.account import Account
from killbill.catalog import Catalog
from killbill.payment_method import PaymentMethod
from killbill.plan_detail import PlanDetail
from killbill.subscription import Subscription
