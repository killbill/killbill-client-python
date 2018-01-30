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
import killbill


class Account(killbill.Resource):
    KILLBILL_API_ACCOUNTS_PREFIX = killbill.Resource.KILLBILL_API_PREFIX + '/accounts'

    def __init__(self, **d):
        super(Account, self).__init__(d)

    def create(self, user=killbill.user, reason=None, comment=None, **options):
        created_account = self.post(self.KILLBILL_API_ACCOUNTS_PREFIX,
                                    self.to_json(),
                                    {},
                                    self.build_options(
                                        user=user,
                                        reason=reason,
                                        comment=comment,
                                        **options
                                    ))
        return self.refresh(created_account, **options)

    def bundles(self, **options):
        return self.get("%s/%s/bundles" % (self.KILLBILL_API_ACCOUNTS_PREFIX, self.accountId),
                        {},
                        self.build_options(**options))
