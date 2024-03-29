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



class AdminPayment(object):
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
        'last_success_payment_state': 'Str',
        'current_payment_state_name': 'Str',
        'transaction_status': 'Str'
    }

    attribute_map = {
        'last_success_payment_state': 'lastSuccessPaymentState',
        'current_payment_state_name': 'currentPaymentStateName',
        'transaction_status': 'transactionStatus'
    }

    def __init__(self, last_success_payment_state=None, current_payment_state_name=None, transaction_status=None):  # noqa: E501
        """AdminPayment - a model defined in Swagger"""  # noqa: E501

        self._last_success_payment_state = None
        self._current_payment_state_name = None
        self._transaction_status = None
        self.discriminator = None

        if last_success_payment_state is not None:
            self.last_success_payment_state = last_success_payment_state
        if current_payment_state_name is not None:
            self.current_payment_state_name = current_payment_state_name
        if transaction_status is not None:
            self.transaction_status = transaction_status

    @property
    def last_success_payment_state(self):
        """Gets the last_success_payment_state of this AdminPayment.  # noqa: E501


        :return: The last_success_payment_state of this AdminPayment.  # noqa: E501
        :rtype: Str
        """
        return self._last_success_payment_state

    @last_success_payment_state.setter
    def last_success_payment_state(self, last_success_payment_state):
        """Sets the last_success_payment_state of this AdminPayment.


        :param last_success_payment_state: The last_success_payment_state of this AdminPayment.  # noqa: E501
        :type: Str
        """


        self._last_success_payment_state = last_success_payment_state

    @property
    def current_payment_state_name(self):
        """Gets the current_payment_state_name of this AdminPayment.  # noqa: E501


        :return: The current_payment_state_name of this AdminPayment.  # noqa: E501
        :rtype: Str
        """
        return self._current_payment_state_name

    @current_payment_state_name.setter
    def current_payment_state_name(self, current_payment_state_name):
        """Sets the current_payment_state_name of this AdminPayment.


        :param current_payment_state_name: The current_payment_state_name of this AdminPayment.  # noqa: E501
        :type: Str
        """


        self._current_payment_state_name = current_payment_state_name

    @property
    def transaction_status(self):
        """Gets the transaction_status of this AdminPayment.  # noqa: E501


        :return: The transaction_status of this AdminPayment.  # noqa: E501
        :rtype: Str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this AdminPayment.


        :param transaction_status: The transaction_status of this AdminPayment.  # noqa: E501
        :type: Str
        """


        self._transaction_status = transaction_status

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
        if not isinstance(other, AdminPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
