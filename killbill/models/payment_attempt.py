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



class PaymentAttempt(object):
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
        'account_id': 'Str',
        'payment_method_id': 'Str',
        'payment_external_key': 'Str',
        'transaction_id': 'Str',
        'transaction_external_key': 'Str',
        'transaction_type': 'Str',
        'effective_date': 'Datetime',
        'state_name': 'Str',
        'amount': 'Float',
        'currency': 'Str',
        'plugin_name': 'Str',
        'plugin_properties': 'List[PluginProperty]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'payment_method_id': 'paymentMethodId',
        'payment_external_key': 'paymentExternalKey',
        'transaction_id': 'transactionId',
        'transaction_external_key': 'transactionExternalKey',
        'transaction_type': 'transactionType',
        'effective_date': 'effectiveDate',
        'state_name': 'stateName',
        'amount': 'amount',
        'currency': 'currency',
        'plugin_name': 'pluginName',
        'plugin_properties': 'pluginProperties',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, payment_method_id=None, payment_external_key=None, transaction_id=None, transaction_external_key=None, transaction_type=None, effective_date=None, state_name=None, amount=None, currency=None, plugin_name=None, plugin_properties=None, audit_logs=None):  # noqa: E501
        """PaymentAttempt - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._payment_method_id = None
        self._payment_external_key = None
        self._transaction_id = None
        self._transaction_external_key = None
        self._transaction_type = None
        self._effective_date = None
        self._state_name = None
        self._amount = None
        self._currency = None
        self._plugin_name = None
        self._plugin_properties = None
        self._audit_logs = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if payment_external_key is not None:
            self.payment_external_key = payment_external_key
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_external_key is not None:
            self.transaction_external_key = transaction_external_key
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if effective_date is not None:
            self.effective_date = effective_date
        if state_name is not None:
            self.state_name = state_name
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_properties is not None:
            self.plugin_properties = plugin_properties
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this PaymentAttempt.  # noqa: E501


        :return: The account_id of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PaymentAttempt.


        :param account_id: The account_id of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._account_id = account_id

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this PaymentAttempt.  # noqa: E501


        :return: The payment_method_id of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this PaymentAttempt.


        :param payment_method_id: The payment_method_id of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._payment_method_id = payment_method_id

    @property
    def payment_external_key(self):
        """Gets the payment_external_key of this PaymentAttempt.  # noqa: E501


        :return: The payment_external_key of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._payment_external_key

    @payment_external_key.setter
    def payment_external_key(self, payment_external_key):
        """Sets the payment_external_key of this PaymentAttempt.


        :param payment_external_key: The payment_external_key of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._payment_external_key = payment_external_key

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PaymentAttempt.  # noqa: E501


        :return: The transaction_id of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PaymentAttempt.


        :param transaction_id: The transaction_id of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._transaction_id = transaction_id

    @property
    def transaction_external_key(self):
        """Gets the transaction_external_key of this PaymentAttempt.  # noqa: E501


        :return: The transaction_external_key of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_external_key

    @transaction_external_key.setter
    def transaction_external_key(self, transaction_external_key):
        """Sets the transaction_external_key of this PaymentAttempt.


        :param transaction_external_key: The transaction_external_key of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._transaction_external_key = transaction_external_key

    @property
    def transaction_type(self):
        """Gets the transaction_type of this PaymentAttempt.  # noqa: E501


        :return: The transaction_type of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this PaymentAttempt.


        :param transaction_type: The transaction_type of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._transaction_type = transaction_type

    @property
    def effective_date(self):
        """Gets the effective_date of this PaymentAttempt.  # noqa: E501


        :return: The effective_date of this PaymentAttempt.  # noqa: E501
        :rtype: Datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this PaymentAttempt.


        :param effective_date: The effective_date of this PaymentAttempt.  # noqa: E501
        :type: Datetime
        """


        self._effective_date = effective_date

    @property
    def state_name(self):
        """Gets the state_name of this PaymentAttempt.  # noqa: E501


        :return: The state_name of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name):
        """Sets the state_name of this PaymentAttempt.


        :param state_name: The state_name of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._state_name = state_name

    @property
    def amount(self):
        """Gets the amount of this PaymentAttempt.  # noqa: E501

        Transaction amount, required except for void operations  # noqa: E501

        :return: The amount of this PaymentAttempt.  # noqa: E501
        :rtype: Float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentAttempt.

        Transaction amount, required except for void operations  # noqa: E501

        :param amount: The amount of this PaymentAttempt.  # noqa: E501
        :type: Float
        """


        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this PaymentAttempt.  # noqa: E501

        Amount currency (account currency unless specified)  # noqa: E501

        :return: The currency of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentAttempt.

        Amount currency (account currency unless specified)  # noqa: E501

        :param currency: The currency of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._currency = currency

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PaymentAttempt.  # noqa: E501


        :return: The plugin_name of this PaymentAttempt.  # noqa: E501
        :rtype: Str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PaymentAttempt.


        :param plugin_name: The plugin_name of this PaymentAttempt.  # noqa: E501
        :type: Str
        """


        self._plugin_name = plugin_name

    @property
    def plugin_properties(self):
        """Gets the plugin_properties of this PaymentAttempt.  # noqa: E501


        :return: The plugin_properties of this PaymentAttempt.  # noqa: E501
        :rtype: List[PluginProperty]
        """
        return self._plugin_properties

    @plugin_properties.setter
    def plugin_properties(self, plugin_properties):
        """Sets the plugin_properties of this PaymentAttempt.


        :param plugin_properties: The plugin_properties of this PaymentAttempt.  # noqa: E501
        :type: List[PluginProperty]
        """


        self._plugin_properties = plugin_properties

    @property
    def audit_logs(self):
        """Gets the audit_logs of this PaymentAttempt.  # noqa: E501


        :return: The audit_logs of this PaymentAttempt.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this PaymentAttempt.


        :param audit_logs: The audit_logs of this PaymentAttempt.  # noqa: E501
        :type: List[AuditLog]
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
        if not isinstance(other, PaymentAttempt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
