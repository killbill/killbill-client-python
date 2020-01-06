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



class Tag(object):
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
        'tag_id': 'Str',
        'object_type': 'Str',
        'object_id': 'Str',
        'tag_definition_id': 'Str',
        'tag_definition_name': 'Str',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'tag_id': 'tagId',
        'object_type': 'objectType',
        'object_id': 'objectId',
        'tag_definition_id': 'tagDefinitionId',
        'tag_definition_name': 'tagDefinitionName',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, tag_id=None, object_type=None, object_id=None, tag_definition_id=None, tag_definition_name=None, audit_logs=None):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501

        self._tag_id = None
        self._object_type = None
        self._object_id = None
        self._tag_definition_id = None
        self._tag_definition_name = None
        self._audit_logs = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if object_type is not None:
            self.object_type = object_type
        if object_id is not None:
            self.object_id = object_id
        if tag_definition_id is not None:
            self.tag_definition_id = tag_definition_id
        if tag_definition_name is not None:
            self.tag_definition_name = tag_definition_name
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def tag_id(self):
        """Gets the tag_id of this Tag.  # noqa: E501


        :return: The tag_id of this Tag.  # noqa: E501
        :rtype: Str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this Tag.


        :param tag_id: The tag_id of this Tag.  # noqa: E501
        :type: Str
        """


        self._tag_id = tag_id

    @property
    def object_type(self):
        """Gets the object_type of this Tag.  # noqa: E501


        :return: The object_type of this Tag.  # noqa: E501
        :rtype: Str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Tag.


        :param object_type: The object_type of this Tag.  # noqa: E501
        :type: Str
        """


        self._object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this Tag.  # noqa: E501


        :return: The object_id of this Tag.  # noqa: E501
        :rtype: Str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this Tag.


        :param object_id: The object_id of this Tag.  # noqa: E501
        :type: Str
        """


        self._object_id = object_id

    @property
    def tag_definition_id(self):
        """Gets the tag_definition_id of this Tag.  # noqa: E501


        :return: The tag_definition_id of this Tag.  # noqa: E501
        :rtype: Str
        """
        return self._tag_definition_id

    @tag_definition_id.setter
    def tag_definition_id(self, tag_definition_id):
        """Sets the tag_definition_id of this Tag.


        :param tag_definition_id: The tag_definition_id of this Tag.  # noqa: E501
        :type: Str
        """


        self._tag_definition_id = tag_definition_id

    @property
    def tag_definition_name(self):
        """Gets the tag_definition_name of this Tag.  # noqa: E501


        :return: The tag_definition_name of this Tag.  # noqa: E501
        :rtype: Str
        """
        return self._tag_definition_name

    @tag_definition_name.setter
    def tag_definition_name(self, tag_definition_name):
        """Sets the tag_definition_name of this Tag.


        :param tag_definition_name: The tag_definition_name of this Tag.  # noqa: E501
        :type: Str
        """


        self._tag_definition_name = tag_definition_name

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Tag.  # noqa: E501


        :return: The audit_logs of this Tag.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Tag.


        :param audit_logs: The audit_logs of this Tag.  # noqa: E501
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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
