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



class Plan(object):
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
        'name': 'Str',
        'pretty_name': 'Str',
        'recurring_billing_mode': 'Str',
        'billing_period': 'Str',
        'phases': 'List[Phase]'
    }

    attribute_map = {
        'name': 'name',
        'pretty_name': 'prettyName',
        'recurring_billing_mode': 'recurringBillingMode',
        'billing_period': 'billingPeriod',
        'phases': 'phases'
    }

    def __init__(self, name=None, pretty_name=None, recurring_billing_mode=None, billing_period=None, phases=None):  # noqa: E501
        """Plan - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._pretty_name = None
        self._recurring_billing_mode = None
        self._billing_period = None
        self._phases = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if pretty_name is not None:
            self.pretty_name = pretty_name
        if recurring_billing_mode is not None:
            self.recurring_billing_mode = recurring_billing_mode
        if billing_period is not None:
            self.billing_period = billing_period
        if phases is not None:
            self.phases = phases

    @property
    def name(self):
        """Gets the name of this Plan.  # noqa: E501


        :return: The name of this Plan.  # noqa: E501
        :rtype: Str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plan.


        :param name: The name of this Plan.  # noqa: E501
        :type: Str
        """


        self._name = name

    @property
    def pretty_name(self):
        """Gets the pretty_name of this Plan.  # noqa: E501


        :return: The pretty_name of this Plan.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_name

    @pretty_name.setter
    def pretty_name(self, pretty_name):
        """Sets the pretty_name of this Plan.


        :param pretty_name: The pretty_name of this Plan.  # noqa: E501
        :type: Str
        """


        self._pretty_name = pretty_name

    @property
    def recurring_billing_mode(self):
        """Gets the recurring_billing_mode of this Plan.  # noqa: E501


        :return: The recurring_billing_mode of this Plan.  # noqa: E501
        :rtype: Str
        """
        return self._recurring_billing_mode

    @recurring_billing_mode.setter
    def recurring_billing_mode(self, recurring_billing_mode):
        """Sets the recurring_billing_mode of this Plan.


        :param recurring_billing_mode: The recurring_billing_mode of this Plan.  # noqa: E501
        :type: Str
        """


        self._recurring_billing_mode = recurring_billing_mode

    @property
    def billing_period(self):
        """Gets the billing_period of this Plan.  # noqa: E501


        :return: The billing_period of this Plan.  # noqa: E501
        :rtype: Str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this Plan.


        :param billing_period: The billing_period of this Plan.  # noqa: E501
        :type: Str
        """


        self._billing_period = billing_period

    @property
    def phases(self):
        """Gets the phases of this Plan.  # noqa: E501


        :return: The phases of this Plan.  # noqa: E501
        :rtype: List[Phase]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """Sets the phases of this Plan.


        :param phases: The phases of this Plan.  # noqa: E501
        :type: List[Phase]
        """


        self._phases = phases

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
        if not isinstance(other, Plan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
