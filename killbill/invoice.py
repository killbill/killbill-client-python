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


class Invoice(killbill.Resource):
    KILLBILL_API_INVOICE_PREFIX = killbill.Resource.KILLBILL_API_PREFIX + '/invoices'

    def __init__(self, **d):
        super(Invoice, self).__init__(d)

    @classmethod
    def find_by_id_or_number(cls, id_or_number, with_items=True, audit="NONE", **options):
        relative_url = "%s/%s" % (cls.KILLBILL_API_INVOICE_PREFIX, id_or_number)
        query_params = {
            'withItems': with_items,
            'audit': audit
        }
        return cls.get(relative_url, query_params, cls.build_options(**options))

    @classmethod
    def as_html(cls, invoice_id, **options):
        relative_url = "%s/%s/html" % (cls.KILLBILL_API_INVOICE_PREFIX, invoice_id)
        return cls.get(relative_url, {}, cls.build_options(accept='text/html', **options))
