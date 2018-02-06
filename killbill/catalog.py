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
from killbill.plan_detail import PlanDetail


class Catalog(killbill.Resource):
    KILLBILL_API_CATALOG_PREFIX = killbill.Resource.KILLBILL_API_PREFIX + '/catalog'

    def __init__(self, **d):
        super(Catalog, self).__init__(d)

    @classmethod
    def available_addons(cls, base_product_name, **options):
        relative_url = "%s/availableAddons" % cls.KILLBILL_API_CATALOG_PREFIX
        query_params = {
            'baseProductName': base_product_name
        }
        return PlanDetail.get(relative_url, query_params, PlanDetail.build_options(**options))

    @classmethod
    def available_base_plans(cls, **options):
        relative_url = "%s/availableBasePlans" % cls.KILLBILL_API_CATALOG_PREFIX
        query_params = {}
        return PlanDetail.get(relative_url, query_params, PlanDetail.build_options(**options))
