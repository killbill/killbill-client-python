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



class Product(object):
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
        'type': 'Str',
        'name': 'Str',
        'pretty_name': 'Str',
        'plans': 'List[Plan]',
        'included': 'List[Str]',
        'available': 'List[Str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'pretty_name': 'prettyName',
        'plans': 'plans',
        'included': 'included',
        'available': 'available'
    }

    def __init__(self, type=None, name=None, pretty_name=None, plans=None, included=None, available=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._name = None
        self._pretty_name = None
        self._plans = None
        self._included = None
        self._available = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if pretty_name is not None:
            self.pretty_name = pretty_name
        if plans is not None:
            self.plans = plans
        if included is not None:
            self.included = included
        if available is not None:
            self.available = available

    @property
    def type(self):
        """Gets the type of this Product.  # noqa: E501


        :return: The type of this Product.  # noqa: E501
        :rtype: Str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Product.


        :param type: The type of this Product.  # noqa: E501
        :type: Str
        """


        self._type = type

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501


        :return: The name of this Product.  # noqa: E501
        :rtype: Str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.


        :param name: The name of this Product.  # noqa: E501
        :type: Str
        """


        self._name = name

    @property
    def pretty_name(self):
        """Gets the pretty_name of this Product.  # noqa: E501


        :return: The pretty_name of this Product.  # noqa: E501
        :rtype: Str
        """
        return self._pretty_name

    @pretty_name.setter
    def pretty_name(self, pretty_name):
        """Sets the pretty_name of this Product.


        :param pretty_name: The pretty_name of this Product.  # noqa: E501
        :type: Str
        """


        self._pretty_name = pretty_name

    @property
    def plans(self):
        """Gets the plans of this Product.  # noqa: E501


        :return: The plans of this Product.  # noqa: E501
        :rtype: List[Plan]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        """Sets the plans of this Product.


        :param plans: The plans of this Product.  # noqa: E501
        :type: List[Plan]
        """


        self._plans = plans

    @property
    def included(self):
        """Gets the included of this Product.  # noqa: E501


        :return: The included of this Product.  # noqa: E501
        :rtype: List[Str]
        """
        return self._included

    @included.setter
    def included(self, included):
        """Sets the included of this Product.


        :param included: The included of this Product.  # noqa: E501
        :type: List[Str]
        """


        self._included = included

    @property
    def available(self):
        """Gets the available of this Product.  # noqa: E501


        :return: The available of this Product.  # noqa: E501
        :rtype: List[Str]
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this Product.


        :param available: The available of this Product.  # noqa: E501
        :type: List[Str]
        """


        self._available = available

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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
