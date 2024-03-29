# coding: utf-8

#
# Copyright 2010-2014 Ning, Inc.
# Copyright 2014-2020 Groupon, Inc
# Copyright 2020-2021 Equinix, Inc
# Copyright 2014-2021 The Billing Project, LLC
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

    OpenAPI spec version: 0.24.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class UsagePrice(object):
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
        'usage_name': 'Str',
        'usage_type': 'Str',
        'billing_mode': 'Str',
        'tier_block_policy': 'Str',
        'tier_prices': 'List[TierPrice]'
    }

    attribute_map = {
        'usage_name': 'usageName',
        'usage_type': 'usageType',
        'billing_mode': 'billingMode',
        'tier_block_policy': 'tierBlockPolicy',
        'tier_prices': 'tierPrices'
    }

    def __init__(self, usage_name=None, usage_type=None, billing_mode=None, tier_block_policy=None, tier_prices=None):  # noqa: E501
        """UsagePrice - a model defined in Swagger"""  # noqa: E501

        self._usage_name = None
        self._usage_type = None
        self._billing_mode = None
        self._tier_block_policy = None
        self._tier_prices = None
        self.discriminator = None

        if usage_name is not None:
            self.usage_name = usage_name
        if usage_type is not None:
            self.usage_type = usage_type
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if tier_block_policy is not None:
            self.tier_block_policy = tier_block_policy
        if tier_prices is not None:
            self.tier_prices = tier_prices

    @property
    def usage_name(self):
        """Gets the usage_name of this UsagePrice.  # noqa: E501


        :return: The usage_name of this UsagePrice.  # noqa: E501
        :rtype: Str
        """
        return self._usage_name

    @usage_name.setter
    def usage_name(self, usage_name):
        """Sets the usage_name of this UsagePrice.


        :param usage_name: The usage_name of this UsagePrice.  # noqa: E501
        :type: Str
        """


        self._usage_name = usage_name

    @property
    def usage_type(self):
        """Gets the usage_type of this UsagePrice.  # noqa: E501


        :return: The usage_type of this UsagePrice.  # noqa: E501
        :rtype: Str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this UsagePrice.


        :param usage_type: The usage_type of this UsagePrice.  # noqa: E501
        :type: Str
        """


        self._usage_type = usage_type

    @property
    def billing_mode(self):
        """Gets the billing_mode of this UsagePrice.  # noqa: E501


        :return: The billing_mode of this UsagePrice.  # noqa: E501
        :rtype: Str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this UsagePrice.


        :param billing_mode: The billing_mode of this UsagePrice.  # noqa: E501
        :type: Str
        """


        self._billing_mode = billing_mode

    @property
    def tier_block_policy(self):
        """Gets the tier_block_policy of this UsagePrice.  # noqa: E501


        :return: The tier_block_policy of this UsagePrice.  # noqa: E501
        :rtype: Str
        """
        return self._tier_block_policy

    @tier_block_policy.setter
    def tier_block_policy(self, tier_block_policy):
        """Sets the tier_block_policy of this UsagePrice.


        :param tier_block_policy: The tier_block_policy of this UsagePrice.  # noqa: E501
        :type: Str
        """


        self._tier_block_policy = tier_block_policy

    @property
    def tier_prices(self):
        """Gets the tier_prices of this UsagePrice.  # noqa: E501


        :return: The tier_prices of this UsagePrice.  # noqa: E501
        :rtype: List[TierPrice]
        """
        return self._tier_prices

    @tier_prices.setter
    def tier_prices(self, tier_prices):
        """Sets the tier_prices of this UsagePrice.


        :param tier_prices: The tier_prices of this UsagePrice.  # noqa: E501
        :type: List[TierPrice]
        """


        self._tier_prices = tier_prices

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
        if not isinstance(other, UsagePrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
