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



class RolledUpUsage(object):
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
        'subscription_id': 'Str',
        'start_date': 'Date',
        'end_date': 'Date',
        'rolled_up_units': 'List[RolledUpUnit]'
    }

    attribute_map = {
        'subscription_id': 'subscriptionId',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'rolled_up_units': 'rolledUpUnits'
    }

    def __init__(self, subscription_id=None, start_date=None, end_date=None, rolled_up_units=None):  # noqa: E501
        """RolledUpUsage - a model defined in Swagger"""  # noqa: E501

        self._subscription_id = None
        self._start_date = None
        self._end_date = None
        self._rolled_up_units = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if rolled_up_units is not None:
            self.rolled_up_units = rolled_up_units

    @property
    def subscription_id(self):
        """Gets the subscription_id of this RolledUpUsage.  # noqa: E501


        :return: The subscription_id of this RolledUpUsage.  # noqa: E501
        :rtype: Str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this RolledUpUsage.


        :param subscription_id: The subscription_id of this RolledUpUsage.  # noqa: E501
        :type: Str
        """


        self._subscription_id = subscription_id

    @property
    def start_date(self):
        """Gets the start_date of this RolledUpUsage.  # noqa: E501


        :return: The start_date of this RolledUpUsage.  # noqa: E501
        :rtype: Date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RolledUpUsage.


        :param start_date: The start_date of this RolledUpUsage.  # noqa: E501
        :type: Date
        """


        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this RolledUpUsage.  # noqa: E501


        :return: The end_date of this RolledUpUsage.  # noqa: E501
        :rtype: Date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RolledUpUsage.


        :param end_date: The end_date of this RolledUpUsage.  # noqa: E501
        :type: Date
        """


        self._end_date = end_date

    @property
    def rolled_up_units(self):
        """Gets the rolled_up_units of this RolledUpUsage.  # noqa: E501


        :return: The rolled_up_units of this RolledUpUsage.  # noqa: E501
        :rtype: List[RolledUpUnit]
        """
        return self._rolled_up_units

    @rolled_up_units.setter
    def rolled_up_units(self, rolled_up_units):
        """Sets the rolled_up_units of this RolledUpUsage.


        :param rolled_up_units: The rolled_up_units of this RolledUpUsage.  # noqa: E501
        :type: List[RolledUpUnit]
        """


        self._rolled_up_units = rolled_up_units

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
        if not isinstance(other, RolledUpUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
