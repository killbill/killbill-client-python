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

from killbill.models.unit_usage_record import UnitUsageRecord  # noqa: F401,E501


class SubscriptionUsageRecord(object):
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
        'subscription_id': 'str',
        'tracking_id': 'str',
        'unit_usage_records': 'list[UnitUsageRecord]'
    }

    attribute_map = {
        'subscription_id': 'subscriptionId',
        'tracking_id': 'trackingId',
        'unit_usage_records': 'unitUsageRecords'
    }

    def __init__(self, subscription_id=None, tracking_id=None, unit_usage_records=None):  # noqa: E501
        """SubscriptionUsageRecord - a model defined in Swagger"""  # noqa: E501

        self._subscription_id = None
        self._tracking_id = None
        self._unit_usage_records = None
        self.discriminator = None

        self.subscription_id = subscription_id
        if tracking_id is not None:
            self.tracking_id = tracking_id
        self.unit_usage_records = unit_usage_records

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SubscriptionUsageRecord.  # noqa: E501


        :return: The subscription_id of this SubscriptionUsageRecord.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SubscriptionUsageRecord.


        :param subscription_id: The subscription_id of this SubscriptionUsageRecord.  # noqa: E501
        :type: str
        """
        if subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def tracking_id(self):
        """Gets the tracking_id of this SubscriptionUsageRecord.  # noqa: E501


        :return: The tracking_id of this SubscriptionUsageRecord.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this SubscriptionUsageRecord.


        :param tracking_id: The tracking_id of this SubscriptionUsageRecord.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def unit_usage_records(self):
        """Gets the unit_usage_records of this SubscriptionUsageRecord.  # noqa: E501


        :return: The unit_usage_records of this SubscriptionUsageRecord.  # noqa: E501
        :rtype: list[UnitUsageRecord]
        """
        return self._unit_usage_records

    @unit_usage_records.setter
    def unit_usage_records(self, unit_usage_records):
        """Sets the unit_usage_records of this SubscriptionUsageRecord.


        :param unit_usage_records: The unit_usage_records of this SubscriptionUsageRecord.  # noqa: E501
        :type: list[UnitUsageRecord]
        """
        if unit_usage_records is None:
            raise ValueError("Invalid value for `unit_usage_records`, must not be `None`")  # noqa: E501

        self._unit_usage_records = unit_usage_records

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
        if not isinstance(other, SubscriptionUsageRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
