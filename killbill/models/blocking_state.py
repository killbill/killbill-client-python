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

from killbill.models.audit_log import AuditLog  # noqa: F401,E501


class BlockingState(object):
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
        'blocked_id': 'str',
        'state_name': 'str',
        'service': 'str',
        'is_block_change': 'bool',
        'is_block_entitlement': 'bool',
        'is_block_billing': 'bool',
        'effective_date': 'datetime',
        'type': 'str',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'blocked_id': 'blockedId',
        'state_name': 'stateName',
        'service': 'service',
        'is_block_change': 'isBlockChange',
        'is_block_entitlement': 'isBlockEntitlement',
        'is_block_billing': 'isBlockBilling',
        'effective_date': 'effectiveDate',
        'type': 'type',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, blocked_id=None, state_name=None, service=None, is_block_change=False, is_block_entitlement=False, is_block_billing=False, effective_date=None, type=None, audit_logs=None):  # noqa: E501
        """BlockingState - a model defined in Swagger"""  # noqa: E501

        self._blocked_id = None
        self._state_name = None
        self._service = None
        self._is_block_change = None
        self._is_block_entitlement = None
        self._is_block_billing = None
        self._effective_date = None
        self._type = None
        self._audit_logs = None
        self.discriminator = None

        if blocked_id is not None:
            self.blocked_id = blocked_id
        if state_name is not None:
            self.state_name = state_name
        if service is not None:
            self.service = service
        if is_block_change is not None:
            self.is_block_change = is_block_change
        if is_block_entitlement is not None:
            self.is_block_entitlement = is_block_entitlement
        if is_block_billing is not None:
            self.is_block_billing = is_block_billing
        if effective_date is not None:
            self.effective_date = effective_date
        if type is not None:
            self.type = type
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def blocked_id(self):
        """Gets the blocked_id of this BlockingState.  # noqa: E501


        :return: The blocked_id of this BlockingState.  # noqa: E501
        :rtype: str
        """
        return self._blocked_id

    @blocked_id.setter
    def blocked_id(self, blocked_id):
        """Sets the blocked_id of this BlockingState.


        :param blocked_id: The blocked_id of this BlockingState.  # noqa: E501
        :type: str
        """

        self._blocked_id = blocked_id

    @property
    def state_name(self):
        """Gets the state_name of this BlockingState.  # noqa: E501


        :return: The state_name of this BlockingState.  # noqa: E501
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name):
        """Sets the state_name of this BlockingState.


        :param state_name: The state_name of this BlockingState.  # noqa: E501
        :type: str
        """

        self._state_name = state_name

    @property
    def service(self):
        """Gets the service of this BlockingState.  # noqa: E501


        :return: The service of this BlockingState.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this BlockingState.


        :param service: The service of this BlockingState.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def is_block_change(self):
        """Gets the is_block_change of this BlockingState.  # noqa: E501


        :return: The is_block_change of this BlockingState.  # noqa: E501
        :rtype: bool
        """
        return self._is_block_change

    @is_block_change.setter
    def is_block_change(self, is_block_change):
        """Sets the is_block_change of this BlockingState.


        :param is_block_change: The is_block_change of this BlockingState.  # noqa: E501
        :type: bool
        """

        self._is_block_change = is_block_change

    @property
    def is_block_entitlement(self):
        """Gets the is_block_entitlement of this BlockingState.  # noqa: E501


        :return: The is_block_entitlement of this BlockingState.  # noqa: E501
        :rtype: bool
        """
        return self._is_block_entitlement

    @is_block_entitlement.setter
    def is_block_entitlement(self, is_block_entitlement):
        """Sets the is_block_entitlement of this BlockingState.


        :param is_block_entitlement: The is_block_entitlement of this BlockingState.  # noqa: E501
        :type: bool
        """

        self._is_block_entitlement = is_block_entitlement

    @property
    def is_block_billing(self):
        """Gets the is_block_billing of this BlockingState.  # noqa: E501


        :return: The is_block_billing of this BlockingState.  # noqa: E501
        :rtype: bool
        """
        return self._is_block_billing

    @is_block_billing.setter
    def is_block_billing(self, is_block_billing):
        """Sets the is_block_billing of this BlockingState.


        :param is_block_billing: The is_block_billing of this BlockingState.  # noqa: E501
        :type: bool
        """

        self._is_block_billing = is_block_billing

    @property
    def effective_date(self):
        """Gets the effective_date of this BlockingState.  # noqa: E501


        :return: The effective_date of this BlockingState.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this BlockingState.


        :param effective_date: The effective_date of this BlockingState.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def type(self):
        """Gets the type of this BlockingState.  # noqa: E501


        :return: The type of this BlockingState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BlockingState.


        :param type: The type of this BlockingState.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUBSCRIPTION", "SUBSCRIPTION_BUNDLE", "ACCOUNT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def audit_logs(self):
        """Gets the audit_logs of this BlockingState.  # noqa: E501


        :return: The audit_logs of this BlockingState.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this BlockingState.


        :param audit_logs: The audit_logs of this BlockingState.  # noqa: E501
        :type: list[AuditLog]
        """

        self._audit_logs = audit_logs

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
        if not isinstance(other, BlockingState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
