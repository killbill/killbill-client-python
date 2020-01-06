# coding: utf-8

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

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class InvoiceDryRun(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dry_run_type': 'Str',
        'dry_run_action': 'Str',
        'phase_type': 'Str',
        'product_name': 'Str',
        'product_category': 'Str',
        'billing_period': 'Str',
        'price_list_name': 'Str',
        'subscription_id': 'Str',
        'bundle_id': 'Str',
        'effective_date': 'Date',
        'billing_policy': 'Str',
        'price_overrides': 'List[PhasePrice]'
    }

    attribute_map = {
        'dry_run_type': 'dryRunType',
        'dry_run_action': 'dryRunAction',
        'phase_type': 'phaseType',
        'product_name': 'productName',
        'product_category': 'productCategory',
        'billing_period': 'billingPeriod',
        'price_list_name': 'priceListName',
        'subscription_id': 'subscriptionId',
        'bundle_id': 'bundleId',
        'effective_date': 'effectiveDate',
        'billing_policy': 'billingPolicy',
        'price_overrides': 'priceOverrides'
    }

    def __init__(self, dry_run_type=None, dry_run_action=None, phase_type=None, product_name=None, product_category=None, billing_period=None, price_list_name=None, subscription_id=None, bundle_id=None, effective_date=None, billing_policy=None, price_overrides=None):  # noqa: E501
        """InvoiceDryRun - a model defined in Swagger"""  # noqa: E501

        self._dry_run_type = None
        self._dry_run_action = None
        self._phase_type = None
        self._product_name = None
        self._product_category = None
        self._billing_period = None
        self._price_list_name = None
        self._subscription_id = None
        self._bundle_id = None
        self._effective_date = None
        self._billing_policy = None
        self._price_overrides = None
        self.discriminator = None

        if dry_run_type is not None:
            self.dry_run_type = dry_run_type
        if dry_run_action is not None:
            self.dry_run_action = dry_run_action
        if phase_type is not None:
            self.phase_type = phase_type
        if product_name is not None:
            self.product_name = product_name
        if product_category is not None:
            self.product_category = product_category
        if billing_period is not None:
            self.billing_period = billing_period
        if price_list_name is not None:
            self.price_list_name = price_list_name
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if effective_date is not None:
            self.effective_date = effective_date
        if billing_policy is not None:
            self.billing_policy = billing_policy
        if price_overrides is not None:
            self.price_overrides = price_overrides

    @property
    def dry_run_type(self):
        """Gets the dry_run_type of this InvoiceDryRun.  # noqa: E501


        :return: The dry_run_type of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._dry_run_type

    @dry_run_type.setter
    def dry_run_type(self, dry_run_type):
        """Sets the dry_run_type of this InvoiceDryRun.


        :param dry_run_type: The dry_run_type of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._dry_run_type = dry_run_type

    @property
    def dry_run_action(self):
        """Gets the dry_run_action of this InvoiceDryRun.  # noqa: E501


        :return: The dry_run_action of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._dry_run_action

    @dry_run_action.setter
    def dry_run_action(self, dry_run_action):
        """Sets the dry_run_action of this InvoiceDryRun.


        :param dry_run_action: The dry_run_action of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._dry_run_action = dry_run_action

    @property
    def phase_type(self):
        """Gets the phase_type of this InvoiceDryRun.  # noqa: E501


        :return: The phase_type of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._phase_type

    @phase_type.setter
    def phase_type(self, phase_type):
        """Sets the phase_type of this InvoiceDryRun.


        :param phase_type: The phase_type of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._phase_type = phase_type

    @property
    def product_name(self):
        """Gets the product_name of this InvoiceDryRun.  # noqa: E501


        :return: The product_name of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this InvoiceDryRun.


        :param product_name: The product_name of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._product_name = product_name

    @property
    def product_category(self):
        """Gets the product_category of this InvoiceDryRun.  # noqa: E501


        :return: The product_category of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this InvoiceDryRun.


        :param product_category: The product_category of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._product_category = product_category

    @property
    def billing_period(self):
        """Gets the billing_period of this InvoiceDryRun.  # noqa: E501


        :return: The billing_period of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this InvoiceDryRun.


        :param billing_period: The billing_period of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._billing_period = billing_period

    @property
    def price_list_name(self):
        """Gets the price_list_name of this InvoiceDryRun.  # noqa: E501


        :return: The price_list_name of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._price_list_name

    @price_list_name.setter
    def price_list_name(self, price_list_name):
        """Sets the price_list_name of this InvoiceDryRun.


        :param price_list_name: The price_list_name of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._price_list_name = price_list_name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this InvoiceDryRun.  # noqa: E501


        :return: The subscription_id of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this InvoiceDryRun.


        :param subscription_id: The subscription_id of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._subscription_id = subscription_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this InvoiceDryRun.  # noqa: E501


        :return: The bundle_id of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this InvoiceDryRun.


        :param bundle_id: The bundle_id of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._bundle_id = bundle_id

    @property
    def effective_date(self):
        """Gets the effective_date of this InvoiceDryRun.  # noqa: E501


        :return: The effective_date of this InvoiceDryRun.  # noqa: E501
        :rtype: Date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this InvoiceDryRun.


        :param effective_date: The effective_date of this InvoiceDryRun.  # noqa: E501
        :type: Date
        """


        self._effective_date = effective_date

    @property
    def billing_policy(self):
        """Gets the billing_policy of this InvoiceDryRun.  # noqa: E501


        :return: The billing_policy of this InvoiceDryRun.  # noqa: E501
        :rtype: Str
        """
        return self._billing_policy

    @billing_policy.setter
    def billing_policy(self, billing_policy):
        """Sets the billing_policy of this InvoiceDryRun.


        :param billing_policy: The billing_policy of this InvoiceDryRun.  # noqa: E501
        :type: Str
        """


        self._billing_policy = billing_policy

    @property
    def price_overrides(self):
        """Gets the price_overrides of this InvoiceDryRun.  # noqa: E501


        :return: The price_overrides of this InvoiceDryRun.  # noqa: E501
        :rtype: List[PhasePrice]
        """
        return self._price_overrides

    @price_overrides.setter
    def price_overrides(self, price_overrides):
        """Sets the price_overrides of this InvoiceDryRun.


        :param price_overrides: The price_overrides of this InvoiceDryRun.  # noqa: E501
        :type: List[PhasePrice]
        """


        self._price_overrides = price_overrides

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvoiceDryRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
