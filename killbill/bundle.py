#
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
import killbill


class Bundle(killbill.Resource):
    KILLBILL_API_BUNDLE_PREFIX = killbill.Resource.KILLBILL_API_PREFIX + '/bundles'

    def __init__(self, **d):
        super(Bundle, self).__init__(d)

    @classmethod
    def find_all_by_account_id_and_external_key(cls, account_id, external_key=None, **options):
        relative_url = "%s/%s/bundles" % (killbill.Account.KILLBILL_API_ACCOUNTS_PREFIX, account_id)
        query_params = {
            'externalKey': external_key
        }
        return cls.get(relative_url, query_params, cls.build_options(**options))
