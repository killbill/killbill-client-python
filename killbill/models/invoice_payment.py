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



class InvoicePayment(object):
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
        'target_invoice_id': 'Str',
        'account_id': 'Str',
        'payment_id': 'Str',
        'payment_number': 'Str',
        'payment_external_key': 'Str',
        'auth_amount': 'Float',
        'captured_amount': 'Float',
        'purchased_amount': 'Float',
        'refunded_amount': 'Float',
        'credited_amount': 'Float',
        'currency': 'Str',
        'payment_method_id': 'Str',
        'transactions': 'List[PaymentTransaction]',
        'payment_attempts': 'List[PaymentAttempt]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'target_invoice_id': 'targetInvoiceId',
        'account_id': 'accountId',
        'payment_id': 'paymentId',
        'payment_number': 'paymentNumber',
        'payment_external_key': 'paymentExternalKey',
        'auth_amount': 'authAmount',
        'captured_amount': 'capturedAmount',
        'purchased_amount': 'purchasedAmount',
        'refunded_amount': 'refundedAmount',
        'credited_amount': 'creditedAmount',
        'currency': 'currency',
        'payment_method_id': 'paymentMethodId',
        'transactions': 'transactions',
        'payment_attempts': 'paymentAttempts',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, target_invoice_id=None, account_id=None, payment_id=None, payment_number=None, payment_external_key=None, auth_amount=None, captured_amount=None, purchased_amount=None, refunded_amount=None, credited_amount=None, currency=None, payment_method_id=None, transactions=None, payment_attempts=None, audit_logs=None):  # noqa: E501
        """InvoicePayment - a model defined in Swagger"""  # noqa: E501

        self._target_invoice_id = None
        self._account_id = None
        self._payment_id = None
        self._payment_number = None
        self._payment_external_key = None
        self._auth_amount = None
        self._captured_amount = None
        self._purchased_amount = None
        self._refunded_amount = None
        self._credited_amount = None
        self._currency = None
        self._payment_method_id = None
        self._transactions = None
        self._payment_attempts = None
        self._audit_logs = None
        self.discriminator = None

        if target_invoice_id is not None:
            self.target_invoice_id = target_invoice_id
        if account_id is not None:
            self.account_id = account_id
        if payment_id is not None:
            self.payment_id = payment_id
        if payment_number is not None:
            self.payment_number = payment_number
        if payment_external_key is not None:
            self.payment_external_key = payment_external_key
        if auth_amount is not None:
            self.auth_amount = auth_amount
        if captured_amount is not None:
            self.captured_amount = captured_amount
        if purchased_amount is not None:
            self.purchased_amount = purchased_amount
        if refunded_amount is not None:
            self.refunded_amount = refunded_amount
        if credited_amount is not None:
            self.credited_amount = credited_amount
        if currency is not None:
            self.currency = currency
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if transactions is not None:
            self.transactions = transactions
        if payment_attempts is not None:
            self.payment_attempts = payment_attempts
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def target_invoice_id(self):
        """Gets the target_invoice_id of this InvoicePayment.  # noqa: E501


        :return: The target_invoice_id of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._target_invoice_id

    @target_invoice_id.setter
    def target_invoice_id(self, target_invoice_id):
        """Sets the target_invoice_id of this InvoicePayment.


        :param target_invoice_id: The target_invoice_id of this InvoicePayment.  # noqa: E501
        :type: Str
        """

        self._target_invoice_id = target_invoice_id

    @property
    def account_id(self):
        """Gets the account_id of this InvoicePayment.  # noqa: E501


        :return: The account_id of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InvoicePayment.


        :param account_id: The account_id of this InvoicePayment.  # noqa: E501
        :type: Str
        """

        self._account_id = account_id

    @property
    def payment_id(self):
        """Gets the payment_id of this InvoicePayment.  # noqa: E501


        :return: The payment_id of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this InvoicePayment.


        :param payment_id: The payment_id of this InvoicePayment.  # noqa: E501
        :type: Str
        """

        self._payment_id = payment_id

    @property
    def payment_number(self):
        """Gets the payment_number of this InvoicePayment.  # noqa: E501


        :return: The payment_number of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._payment_number

    @payment_number.setter
    def payment_number(self, payment_number):
        """Sets the payment_number of this InvoicePayment.


        :param payment_number: The payment_number of this InvoicePayment.  # noqa: E501
        :type: Str
        """

        self._payment_number = payment_number

    @property
    def payment_external_key(self):
        """Gets the payment_external_key of this InvoicePayment.  # noqa: E501


        :return: The payment_external_key of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._payment_external_key

    @payment_external_key.setter
    def payment_external_key(self, payment_external_key):
        """Sets the payment_external_key of this InvoicePayment.


        :param payment_external_key: The payment_external_key of this InvoicePayment.  # noqa: E501
        :type: Str
        """

        self._payment_external_key = payment_external_key

    @property
    def auth_amount(self):
        """Gets the auth_amount of this InvoicePayment.  # noqa: E501


        :return: The auth_amount of this InvoicePayment.  # noqa: E501
        :rtype: Float
        """
        return self._auth_amount

    @auth_amount.setter
    def auth_amount(self, auth_amount):
        """Sets the auth_amount of this InvoicePayment.


        :param auth_amount: The auth_amount of this InvoicePayment.  # noqa: E501
        :type: Float
        """

        self._auth_amount = auth_amount

    @property
    def captured_amount(self):
        """Gets the captured_amount of this InvoicePayment.  # noqa: E501


        :return: The captured_amount of this InvoicePayment.  # noqa: E501
        :rtype: Float
        """
        return self._captured_amount

    @captured_amount.setter
    def captured_amount(self, captured_amount):
        """Sets the captured_amount of this InvoicePayment.


        :param captured_amount: The captured_amount of this InvoicePayment.  # noqa: E501
        :type: Float
        """

        self._captured_amount = captured_amount

    @property
    def purchased_amount(self):
        """Gets the purchased_amount of this InvoicePayment.  # noqa: E501


        :return: The purchased_amount of this InvoicePayment.  # noqa: E501
        :rtype: Float
        """
        return self._purchased_amount

    @purchased_amount.setter
    def purchased_amount(self, purchased_amount):
        """Sets the purchased_amount of this InvoicePayment.


        :param purchased_amount: The purchased_amount of this InvoicePayment.  # noqa: E501
        :type: Float
        """

        self._purchased_amount = purchased_amount

    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this InvoicePayment.  # noqa: E501


        :return: The refunded_amount of this InvoicePayment.  # noqa: E501
        :rtype: Float
        """
        return self._refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, refunded_amount):
        """Sets the refunded_amount of this InvoicePayment.


        :param refunded_amount: The refunded_amount of this InvoicePayment.  # noqa: E501
        :type: Float
        """

        self._refunded_amount = refunded_amount

    @property
    def credited_amount(self):
        """Gets the credited_amount of this InvoicePayment.  # noqa: E501


        :return: The credited_amount of this InvoicePayment.  # noqa: E501
        :rtype: Float
        """
        return self._credited_amount

    @credited_amount.setter
    def credited_amount(self, credited_amount):
        """Sets the credited_amount of this InvoicePayment.


        :param credited_amount: The credited_amount of this InvoicePayment.  # noqa: E501
        :type: Float
        """

        self._credited_amount = credited_amount

    @property
    def currency(self):
        """Gets the currency of this InvoicePayment.  # noqa: E501


        :return: The currency of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoicePayment.


        :param currency: The currency of this InvoicePayment.  # noqa: E501
        :type: Str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWD", "BTC"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this InvoicePayment.  # noqa: E501


        :return: The payment_method_id of this InvoicePayment.  # noqa: E501
        :rtype: Str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this InvoicePayment.


        :param payment_method_id: The payment_method_id of this InvoicePayment.  # noqa: E501
        :type: Str
        """

        self._payment_method_id = payment_method_id

    @property
    def transactions(self):
        """Gets the transactions of this InvoicePayment.  # noqa: E501


        :return: The transactions of this InvoicePayment.  # noqa: E501
        :rtype: List[PaymentTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this InvoicePayment.


        :param transactions: The transactions of this InvoicePayment.  # noqa: E501
        :type: List[PaymentTransaction]
        """

        self._transactions = transactions

    @property
    def payment_attempts(self):
        """Gets the payment_attempts of this InvoicePayment.  # noqa: E501


        :return: The payment_attempts of this InvoicePayment.  # noqa: E501
        :rtype: List[PaymentAttempt]
        """
        return self._payment_attempts

    @payment_attempts.setter
    def payment_attempts(self, payment_attempts):
        """Sets the payment_attempts of this InvoicePayment.


        :param payment_attempts: The payment_attempts of this InvoicePayment.  # noqa: E501
        :type: List[PaymentAttempt]
        """

        self._payment_attempts = payment_attempts

    @property
    def audit_logs(self):
        """Gets the audit_logs of this InvoicePayment.  # noqa: E501


        :return: The audit_logs of this InvoicePayment.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this InvoicePayment.


        :param audit_logs: The audit_logs of this InvoicePayment.  # noqa: E501
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
        if not isinstance(other, InvoicePayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other