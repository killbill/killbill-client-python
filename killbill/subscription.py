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
import killbill


class Subscription(killbill.Resource):
    KILLBILL_API_ENTITLEMENT_PREFIX = killbill.Resource.KILLBILL_API_PREFIX + '/subscriptions'

    def __init__(self, **d):
        super(Subscription, self).__init__(d)

    def create(self, user=killbill.user, reason=None, comment=None, requested_date=None, call_completion=False, **options):
        query_params = {}

        if call_completion:
            query_params['callCompletion'] = call_completion

        if requested_date:
            query_params['entitlementDate'] = requested_date
            query_params['billingDate'] = requested_date

        created_subscription = self.post(self.KILLBILL_API_ENTITLEMENT_PREFIX,
                                         self.to_json(),
                                         query_params,
                                         self.build_options(
                                             user=user,
                                             reason=reason,
                                             comment=comment,
                                             **options
                                         ))
        return self.refresh(created_subscription, **options)
