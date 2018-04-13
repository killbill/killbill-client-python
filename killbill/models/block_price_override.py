# coding: utf-8

"""
    Copyright 2014-2018 Groupon, Inc
    Copyright 2014-2018 The Billing Project, LLC

    The Billing Project licenses this file to you under the Apache License, version 2.0
    (the "License"); you may not use this file except in compliance with the
    License.  You may obtain a copy of the License at:

     http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
    License for the specific language governing permissions and limitations
    under the License.
"""


"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BlockPriceOverride(object):
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
        'unit_name': 'str',
        'size': 'float',
        'price': 'float',
        'max': 'float'
    }

    attribute_map = {
        'unit_name': 'unitName',
        'size': 'size',
        'price': 'price',
        'max': 'max'
    }

    def __init__(self, unit_name=None, size=None, price=None, max=None):  # noqa: E501
        """BlockPriceOverride - a model defined in Swagger"""  # noqa: E501

        self._unit_name = None
        self._size = None
        self._price = None
        self._max = None
        self.discriminator = None

        if unit_name is not None:
            self.unit_name = unit_name
        if size is not None:
            self.size = size
        if price is not None:
            self.price = price
        if max is not None:
            self.max = max

    @property
    def unit_name(self):
        """Gets the unit_name of this BlockPriceOverride.  # noqa: E501


        :return: The unit_name of this BlockPriceOverride.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this BlockPriceOverride.


        :param unit_name: The unit_name of this BlockPriceOverride.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

    @property
    def size(self):
        """Gets the size of this BlockPriceOverride.  # noqa: E501


        :return: The size of this BlockPriceOverride.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BlockPriceOverride.


        :param size: The size of this BlockPriceOverride.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def price(self):
        """Gets the price of this BlockPriceOverride.  # noqa: E501


        :return: The price of this BlockPriceOverride.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BlockPriceOverride.


        :param price: The price of this BlockPriceOverride.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def max(self):
        """Gets the max of this BlockPriceOverride.  # noqa: E501


        :return: The max of this BlockPriceOverride.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this BlockPriceOverride.


        :param max: The max of this BlockPriceOverride.  # noqa: E501
        :type: float
        """

        self._max = max

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
        if not isinstance(other, BlockPriceOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
