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

    def update(self, **options):
        updated_account = self.put("%s/%s" % (self.KILLBILL_API_ACCOUNTS_PREFIX, self.accountId),
                                   self.to_json(),
                                   {},
                                   self.build_options(**options))
        return self.fromJson(updated_account['body'])

    def bundles(self, **options):
        return killbill.Bundle.get("%s/%s/bundles" % (self.KILLBILL_API_ACCOUNTS_PREFIX, self.accountId),
                                   {},
                                   killbill.Bundle.build_options(**options))

    def close(self, cancel_all_subscriptions, write_off_unpaid_invoices, item_adjust_unpaid_invoices, user, reason=None,
              comment=None, **options):
        return self.delete("%s/%s" % (self.KILLBILL_API_ACCOUNTS_PREFIX, self.accountId),
                           "{}",
                           {
                               'cancelAllSubscriptions': cancel_all_subscriptions,
                               'writeOffUnpaidInvoices': write_off_unpaid_invoices,
                               'itemAdjustUnpaidInvoices': item_adjust_unpaid_invoices
                           },
                           self.build_options(
                               user=user,
                               reason=reason,
                               comment=comment,
                               **options
                           ))

    def invoices(self, with_items=False, with_migration_invoices=False, unpaid_invoices_only=False, audit='NONE',
                 **options):
        return killbill.Invoice.get("%s/%s/invoices" % (self.KILLBILL_API_ACCOUNTS_PREFIX, self.accountId),
                                    {
                                        'withItems': with_items,
                                        'withMigrationInvoices': with_migration_invoices,
                                        'unpaidInvoicesOnly': unpaid_invoices_only,
                                        'audit': audit
                                    },
                                    killbill.Invoice.build_options(**options))

    @classmethod
    def find_by_external_key(cls, external_key, **options):
        query_params = {
            'externalKey': external_key
        }
        return cls.get(cls.KILLBILL_API_ACCOUNTS_PREFIX, query_params, cls.build_options(**options))

    @classmethod
    def find_by_id(cls, account_id, account_with_balance=False, account_with_balance_and_cba=False, audit='NONE',
                   **options):
        relative_url = "%s/%s" % (cls.KILLBILL_API_ACCOUNTS_PREFIX, account_id)
        query_params = {
            'accountWithBalance': account_with_balance,
            'accountWithBalanceAndCBA': account_with_balance_and_cba,
            'audit': audit
        }
        return cls.get(relative_url, query_params, cls.build_options(**options))
