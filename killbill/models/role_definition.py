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



class RoleDefinition(object):
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
        'role': 'Str',
        'permissions': 'List[Str]'
    }

    attribute_map = {
        'role': 'role',
        'permissions': 'permissions'
    }

    def __init__(self, role=None, permissions=None):  # noqa: E501
        """RoleDefinition - a model defined in Swagger"""  # noqa: E501

        self._role = None
        self._permissions = None
        self.discriminator = None

        self.role = role
        self.permissions = permissions

    @property
    def role(self):
        """Gets the role of this RoleDefinition.  # noqa: E501


        :return: The role of this RoleDefinition.  # noqa: E501
        :rtype: Str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleDefinition.


        :param role: The role of this RoleDefinition.  # noqa: E501
        :type: Str
        """


        self._role = role

    @property
    def permissions(self):
        """Gets the permissions of this RoleDefinition.  # noqa: E501


        :return: The permissions of this RoleDefinition.  # noqa: E501
        :rtype: List[Str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoleDefinition.


        :param permissions: The permissions of this RoleDefinition.  # noqa: E501
        :type: List[Str]
        """


        self._permissions = permissions

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
        if not isinstance(other, RoleDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
