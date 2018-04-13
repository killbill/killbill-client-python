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


class OverdueState(object):
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
        'name': 'str',
        'external_message': 'str',
        'days_between_payment_retries': 'list[int]',
        'is_disable_entitlement_and_changes_blocked': 'bool',
        'is_block_changes': 'bool',
        'is_clear_state': 'bool',
        'reevaluation_interval_days': 'int'
    }

    attribute_map = {
        'name': 'name',
        'external_message': 'externalMessage',
        'days_between_payment_retries': 'daysBetweenPaymentRetries',
        'is_disable_entitlement_and_changes_blocked': 'isDisableEntitlementAndChangesBlocked',
        'is_block_changes': 'isBlockChanges',
        'is_clear_state': 'isClearState',
        'reevaluation_interval_days': 'reevaluationIntervalDays'
    }

    def __init__(self, name=None, external_message=None, days_between_payment_retries=None, is_disable_entitlement_and_changes_blocked=False, is_block_changes=False, is_clear_state=False, reevaluation_interval_days=None):  # noqa: E501
        """OverdueState - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._external_message = None
        self._days_between_payment_retries = None
        self._is_disable_entitlement_and_changes_blocked = None
        self._is_block_changes = None
        self._is_clear_state = None
        self._reevaluation_interval_days = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if external_message is not None:
            self.external_message = external_message
        if days_between_payment_retries is not None:
            self.days_between_payment_retries = days_between_payment_retries
        if is_disable_entitlement_and_changes_blocked is not None:
            self.is_disable_entitlement_and_changes_blocked = is_disable_entitlement_and_changes_blocked
        if is_block_changes is not None:
            self.is_block_changes = is_block_changes
        if is_clear_state is not None:
            self.is_clear_state = is_clear_state
        if reevaluation_interval_days is not None:
            self.reevaluation_interval_days = reevaluation_interval_days

    @property
    def name(self):
        """Gets the name of this OverdueState.  # noqa: E501


        :return: The name of this OverdueState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OverdueState.


        :param name: The name of this OverdueState.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def external_message(self):
        """Gets the external_message of this OverdueState.  # noqa: E501


        :return: The external_message of this OverdueState.  # noqa: E501
        :rtype: str
        """
        return self._external_message

    @external_message.setter
    def external_message(self, external_message):
        """Sets the external_message of this OverdueState.


        :param external_message: The external_message of this OverdueState.  # noqa: E501
        :type: str
        """

        self._external_message = external_message

    @property
    def days_between_payment_retries(self):
        """Gets the days_between_payment_retries of this OverdueState.  # noqa: E501


        :return: The days_between_payment_retries of this OverdueState.  # noqa: E501
        :rtype: list[int]
        """
        return self._days_between_payment_retries

    @days_between_payment_retries.setter
    def days_between_payment_retries(self, days_between_payment_retries):
        """Sets the days_between_payment_retries of this OverdueState.


        :param days_between_payment_retries: The days_between_payment_retries of this OverdueState.  # noqa: E501
        :type: list[int]
        """

        self._days_between_payment_retries = days_between_payment_retries

    @property
    def is_disable_entitlement_and_changes_blocked(self):
        """Gets the is_disable_entitlement_and_changes_blocked of this OverdueState.  # noqa: E501


        :return: The is_disable_entitlement_and_changes_blocked of this OverdueState.  # noqa: E501
        :rtype: bool
        """
        return self._is_disable_entitlement_and_changes_blocked

    @is_disable_entitlement_and_changes_blocked.setter
    def is_disable_entitlement_and_changes_blocked(self, is_disable_entitlement_and_changes_blocked):
        """Sets the is_disable_entitlement_and_changes_blocked of this OverdueState.


        :param is_disable_entitlement_and_changes_blocked: The is_disable_entitlement_and_changes_blocked of this OverdueState.  # noqa: E501
        :type: bool
        """

        self._is_disable_entitlement_and_changes_blocked = is_disable_entitlement_and_changes_blocked

    @property
    def is_block_changes(self):
        """Gets the is_block_changes of this OverdueState.  # noqa: E501


        :return: The is_block_changes of this OverdueState.  # noqa: E501
        :rtype: bool
        """
        return self._is_block_changes

    @is_block_changes.setter
    def is_block_changes(self, is_block_changes):
        """Sets the is_block_changes of this OverdueState.


        :param is_block_changes: The is_block_changes of this OverdueState.  # noqa: E501
        :type: bool
        """

        self._is_block_changes = is_block_changes

    @property
    def is_clear_state(self):
        """Gets the is_clear_state of this OverdueState.  # noqa: E501


        :return: The is_clear_state of this OverdueState.  # noqa: E501
        :rtype: bool
        """
        return self._is_clear_state

    @is_clear_state.setter
    def is_clear_state(self, is_clear_state):
        """Sets the is_clear_state of this OverdueState.


        :param is_clear_state: The is_clear_state of this OverdueState.  # noqa: E501
        :type: bool
        """

        self._is_clear_state = is_clear_state

    @property
    def reevaluation_interval_days(self):
        """Gets the reevaluation_interval_days of this OverdueState.  # noqa: E501


        :return: The reevaluation_interval_days of this OverdueState.  # noqa: E501
        :rtype: int
        """
        return self._reevaluation_interval_days

    @reevaluation_interval_days.setter
    def reevaluation_interval_days(self, reevaluation_interval_days):
        """Sets the reevaluation_interval_days of this OverdueState.


        :param reevaluation_interval_days: The reevaluation_interval_days of this OverdueState.  # noqa: E501
        :type: int
        """

        self._reevaluation_interval_days = reevaluation_interval_days

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
        if not isinstance(other, OverdueState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
