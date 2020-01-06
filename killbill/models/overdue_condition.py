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



class OverdueCondition(object):
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
        'time_since_earliest_unpaid_invoice_equals_or_exceeds': 'Duration',
        'control_tag_inclusion': 'Str',
        'control_tag_exclusion': 'Str',
        'number_of_unpaid_invoices_equals_or_exceeds': 'Int',
        'response_for_last_failed_payment': 'List[Str]',
        'total_unpaid_invoice_balance_equals_or_exceeds': 'Float'
    }

    attribute_map = {
        'time_since_earliest_unpaid_invoice_equals_or_exceeds': 'timeSinceEarliestUnpaidInvoiceEqualsOrExceeds',
        'control_tag_inclusion': 'controlTagInclusion',
        'control_tag_exclusion': 'controlTagExclusion',
        'number_of_unpaid_invoices_equals_or_exceeds': 'numberOfUnpaidInvoicesEqualsOrExceeds',
        'response_for_last_failed_payment': 'responseForLastFailedPayment',
        'total_unpaid_invoice_balance_equals_or_exceeds': 'totalUnpaidInvoiceBalanceEqualsOrExceeds'
    }

    def __init__(self, time_since_earliest_unpaid_invoice_equals_or_exceeds=None, control_tag_inclusion=None, control_tag_exclusion=None, number_of_unpaid_invoices_equals_or_exceeds=None, response_for_last_failed_payment=None, total_unpaid_invoice_balance_equals_or_exceeds=None):  # noqa: E501
        """OverdueCondition - a model defined in Swagger"""  # noqa: E501

        self._time_since_earliest_unpaid_invoice_equals_or_exceeds = None
        self._control_tag_inclusion = None
        self._control_tag_exclusion = None
        self._number_of_unpaid_invoices_equals_or_exceeds = None
        self._response_for_last_failed_payment = None
        self._total_unpaid_invoice_balance_equals_or_exceeds = None
        self.discriminator = None

        if time_since_earliest_unpaid_invoice_equals_or_exceeds is not None:
            self.time_since_earliest_unpaid_invoice_equals_or_exceeds = time_since_earliest_unpaid_invoice_equals_or_exceeds
        if control_tag_inclusion is not None:
            self.control_tag_inclusion = control_tag_inclusion
        if control_tag_exclusion is not None:
            self.control_tag_exclusion = control_tag_exclusion
        if number_of_unpaid_invoices_equals_or_exceeds is not None:
            self.number_of_unpaid_invoices_equals_or_exceeds = number_of_unpaid_invoices_equals_or_exceeds
        if response_for_last_failed_payment is not None:
            self.response_for_last_failed_payment = response_for_last_failed_payment
        if total_unpaid_invoice_balance_equals_or_exceeds is not None:
            self.total_unpaid_invoice_balance_equals_or_exceeds = total_unpaid_invoice_balance_equals_or_exceeds

    @property
    def time_since_earliest_unpaid_invoice_equals_or_exceeds(self):
        """Gets the time_since_earliest_unpaid_invoice_equals_or_exceeds of this OverdueCondition.  # noqa: E501


        :return: The time_since_earliest_unpaid_invoice_equals_or_exceeds of this OverdueCondition.  # noqa: E501
        :rtype: Duration
        """
        return self._time_since_earliest_unpaid_invoice_equals_or_exceeds

    @time_since_earliest_unpaid_invoice_equals_or_exceeds.setter
    def time_since_earliest_unpaid_invoice_equals_or_exceeds(self, time_since_earliest_unpaid_invoice_equals_or_exceeds):
        """Sets the time_since_earliest_unpaid_invoice_equals_or_exceeds of this OverdueCondition.


        :param time_since_earliest_unpaid_invoice_equals_or_exceeds: The time_since_earliest_unpaid_invoice_equals_or_exceeds of this OverdueCondition.  # noqa: E501
        :type: Duration
        """


        self._time_since_earliest_unpaid_invoice_equals_or_exceeds = time_since_earliest_unpaid_invoice_equals_or_exceeds

    @property
    def control_tag_inclusion(self):
        """Gets the control_tag_inclusion of this OverdueCondition.  # noqa: E501


        :return: The control_tag_inclusion of this OverdueCondition.  # noqa: E501
        :rtype: Str
        """
        return self._control_tag_inclusion

    @control_tag_inclusion.setter
    def control_tag_inclusion(self, control_tag_inclusion):
        """Sets the control_tag_inclusion of this OverdueCondition.


        :param control_tag_inclusion: The control_tag_inclusion of this OverdueCondition.  # noqa: E501
        :type: Str
        """


        self._control_tag_inclusion = control_tag_inclusion

    @property
    def control_tag_exclusion(self):
        """Gets the control_tag_exclusion of this OverdueCondition.  # noqa: E501


        :return: The control_tag_exclusion of this OverdueCondition.  # noqa: E501
        :rtype: Str
        """
        return self._control_tag_exclusion

    @control_tag_exclusion.setter
    def control_tag_exclusion(self, control_tag_exclusion):
        """Sets the control_tag_exclusion of this OverdueCondition.


        :param control_tag_exclusion: The control_tag_exclusion of this OverdueCondition.  # noqa: E501
        :type: Str
        """


        self._control_tag_exclusion = control_tag_exclusion

    @property
    def number_of_unpaid_invoices_equals_or_exceeds(self):
        """Gets the number_of_unpaid_invoices_equals_or_exceeds of this OverdueCondition.  # noqa: E501


        :return: The number_of_unpaid_invoices_equals_or_exceeds of this OverdueCondition.  # noqa: E501
        :rtype: Int
        """
        return self._number_of_unpaid_invoices_equals_or_exceeds

    @number_of_unpaid_invoices_equals_or_exceeds.setter
    def number_of_unpaid_invoices_equals_or_exceeds(self, number_of_unpaid_invoices_equals_or_exceeds):
        """Sets the number_of_unpaid_invoices_equals_or_exceeds of this OverdueCondition.


        :param number_of_unpaid_invoices_equals_or_exceeds: The number_of_unpaid_invoices_equals_or_exceeds of this OverdueCondition.  # noqa: E501
        :type: Int
        """


        self._number_of_unpaid_invoices_equals_or_exceeds = number_of_unpaid_invoices_equals_or_exceeds

    @property
    def response_for_last_failed_payment(self):
        """Gets the response_for_last_failed_payment of this OverdueCondition.  # noqa: E501


        :return: The response_for_last_failed_payment of this OverdueCondition.  # noqa: E501
        :rtype: List[Str]
        """
        return self._response_for_last_failed_payment

    @response_for_last_failed_payment.setter
    def response_for_last_failed_payment(self, response_for_last_failed_payment):
        """Sets the response_for_last_failed_payment of this OverdueCondition.


        :param response_for_last_failed_payment: The response_for_last_failed_payment of this OverdueCondition.  # noqa: E501
        :type: List[Str]
        """

        allowed_values = ["INVALID_CARD", "EXPIRED_CARD", "LOST_OR_STOLEN_CARD", "DO_NOT_HONOR", "INSUFFICIENT_FUNDS", "DECLINE", "PROCESSING_ERROR", "INVALID_AMOUNT", "DUPLICATE_TRANSACTION", "OTHER"]  # noqa: E501
        if not set(response_for_last_failed_payment).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `response_for_last_failed_payment` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(response_for_last_failed_payment) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._response_for_last_failed_payment = response_for_last_failed_payment

    @property
    def total_unpaid_invoice_balance_equals_or_exceeds(self):
        """Gets the total_unpaid_invoice_balance_equals_or_exceeds of this OverdueCondition.  # noqa: E501


        :return: The total_unpaid_invoice_balance_equals_or_exceeds of this OverdueCondition.  # noqa: E501
        :rtype: Float
        """
        return self._total_unpaid_invoice_balance_equals_or_exceeds

    @total_unpaid_invoice_balance_equals_or_exceeds.setter
    def total_unpaid_invoice_balance_equals_or_exceeds(self, total_unpaid_invoice_balance_equals_or_exceeds):
        """Sets the total_unpaid_invoice_balance_equals_or_exceeds of this OverdueCondition.


        :param total_unpaid_invoice_balance_equals_or_exceeds: The total_unpaid_invoice_balance_equals_or_exceeds of this OverdueCondition.  # noqa: E501
        :type: Float
        """


        self._total_unpaid_invoice_balance_equals_or_exceeds = total_unpaid_invoice_balance_equals_or_exceeds

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
        if not isinstance(other, OverdueCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
