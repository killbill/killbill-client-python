#
# Copyright 2011-2012 Ning, Inc.
#
# Ning licenses this file to you under the Apache License, version 2.0
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

import unittest
from killbill import Account

class TestSerialization(unittest.TestCase):

    def test_should_be_able_to_serialize_account_from_json(self):
        accountJson = '{"accountId":"d9164b72-03b2-4c41-a0e1-8351f17050b4",\
                        "name":"stephane","externalKey":"4ff6022398b3a","email":"stephane@yahoo.com",\
                        "currency":"USD","paymentMethodId":null,"address1":"1769 mission street","address2":"Street Address 2",\
                        "company":"","state":"CA","country":"United States","phone":"4152715447","length":8,"billCycleDay":1,"timeZone":"UTC"}'
        account = Account.fromJson(accountJson)
        self.assertEqual('d9164b72-03b2-4c41-a0e1-8351f17050b4', account.accountId)
        self.assertEqual('stephane', account.name)
        self.assertEqual('4ff6022398b3a', account.externalKey)
        self.assertEqual('stephane@yahoo.com', account.email)
        self.assertEqual('USD', account.currency)
        self.assertEqual(None, account.paymentMethodId)
        self.assertEqual('1769 mission street', account.address1)
        self.assertEqual('Street Address 2', account.address2)
        self.assertEqual('', account.company)
        self.assertEqual('CA', account.state)
        self.assertEqual('United States', account.country)
        self.assertEqual('4152715447', account.phone)
        self.assertEqual(8, account.length)
        self.assertEqual(1, account.billCycleDay)
        self.assertEqual('UTC', account.timeZone)

if __name__ == '__main__':
    unittest.main()
