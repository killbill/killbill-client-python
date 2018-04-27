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

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class Limit(object):
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
        'unit': 'Str',
        'max': 'Str',
        'min': 'Str'
    }

    attribute_map = {
        'unit': 'unit',
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, unit=None, max=None, min=None):  # noqa: E501
        """Limit - a model defined in Swagger"""  # noqa: E501

        self._unit = None
        self._max = None
        self._min = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def unit(self):
        """Gets the unit of this Limit.  # noqa: E501


        :return: The unit of this Limit.  # noqa: E501
        :rtype: Str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Limit.


        :param unit: The unit of this Limit.  # noqa: E501
        :type: Str
        """

        self._unit = unit

    @property
    def max(self):
        """Gets the max of this Limit.  # noqa: E501


        :return: The max of this Limit.  # noqa: E501
        :rtype: Str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Limit.


        :param max: The max of this Limit.  # noqa: E501
        :type: Str
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this Limit.  # noqa: E501


        :return: The min of this Limit.  # noqa: E501
        :rtype: Str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Limit.


        :param min: The min of this Limit.  # noqa: E501
        :type: Str
        """

        self._min = min

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
        if not isinstance(other, Limit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other