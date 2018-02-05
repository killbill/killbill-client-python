#
# Copyright 2018 Quentral S.r.l.
# Copyright 2014-2018 The Billing Project, LLC
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


class PaymentMethod(killbill.Resource):
    KILLBILL_API_PAYMENT_METHODS_PREFIX = killbill.Resource.KILLBILL_API_PREFIX + '/paymentMethods'

    def __init__(self, **d):
        super(PaymentMethod, self).__init__(d)

    def create(self, is_default=True, user=killbill.user, reason=None, comment=None, **options):
        created_payment_method = self.post("%s/%s/paymentMethods" %
                                           (killbill.Account.KILLBILL_API_ACCOUNTS_PREFIX, self.accountId),
                                           self.to_json(),
                                           {'isDefault': is_default},
                                           self.build_options(
                                               user=user,
                                               reason=reason,
                                               comment=comment,
                                               **options
                                           ))
        return self.refresh(created_payment_method, **options)

    def set_default(self, user=killbill.user, reason=None, comment=None, **options):
        set_default = self.put("%s/%s/paymentMethods/%s/setDefault" %
                               (killbill.Account.KILLBILL_API_ACCOUNTS_PREFIX,
                                self.accountId, self.paymentMethodId),
                               "{}",
                               {},
                               self.build_options(
                                   user=user,
                                   reason=reason,
                                   comment=comment,
                                   **options
                               ))
        return self.refresh(set_default, **options)

    def destroy(self, delete_default_pm_with_auto_pay_off=False, force_default_pm_deletion=False, user=killbill.user,
                reason=None, comment=None, **options):
        return self.delete("%s/%s" % (self.KILLBILL_API_PAYMENT_METHODS_PREFIX, self.paymentMethodId),
                           "{}",
                           {'deleteDefaultPmWithAutoPayOff': delete_default_pm_with_auto_pay_off,
                            'forceDefaultPmDeletion': force_default_pm_deletion},
                           self.build_options(
                               user=user,
                               reason=reason,
                               comment=comment,
                               **options
                           ))

    @classmethod
    def find_all_by_account_id(cls, account_id, with_plugin_info=False, **options):
        relative_url = "%s/%s/paymentMethods" % (killbill.Account.KILLBILL_API_ACCOUNTS_PREFIX, account_id)
        query_params = {
            'withPluginInfo': with_plugin_info
        }
        return cls.get(relative_url, query_params, cls.build_options(**options))
