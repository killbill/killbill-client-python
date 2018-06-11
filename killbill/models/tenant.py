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

    OpenAPI spec version: 0.19.17-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class Tenant(object):
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
        'tenant_id': 'Str',
        'external_key': 'Str',
        'api_key': 'Str',
        'api_secret': 'Str',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'external_key': 'externalKey',
        'api_key': 'apiKey',
        'api_secret': 'apiSecret',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, tenant_id=None, external_key=None, api_key=None, api_secret=None, audit_logs=None):  # noqa: E501
        """Tenant - a model defined in Swagger"""  # noqa: E501

        self._tenant_id = None
        self._external_key = None
        self._api_key = None
        self._api_secret = None
        self._audit_logs = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if external_key is not None:
            self.external_key = external_key
        self.api_key = api_key
        self.api_secret = api_secret
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Tenant.  # noqa: E501


        :return: The tenant_id of this Tenant.  # noqa: E501
        :rtype: Str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Tenant.


        :param tenant_id: The tenant_id of this Tenant.  # noqa: E501
        :type: Str
        """


        self._tenant_id = tenant_id

    @property
    def external_key(self):
        """Gets the external_key of this Tenant.  # noqa: E501


        :return: The external_key of this Tenant.  # noqa: E501
        :rtype: Str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this Tenant.


        :param external_key: The external_key of this Tenant.  # noqa: E501
        :type: Str
        """


        self._external_key = external_key

    @property
    def api_key(self):
        """Gets the api_key of this Tenant.  # noqa: E501


        :return: The api_key of this Tenant.  # noqa: E501
        :rtype: Str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Tenant.


        :param api_key: The api_key of this Tenant.  # noqa: E501
        :type: Str
        """


        self._api_key = api_key

    @property
    def api_secret(self):
        """Gets the api_secret of this Tenant.  # noqa: E501


        :return: The api_secret of this Tenant.  # noqa: E501
        :rtype: Str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        """Sets the api_secret of this Tenant.


        :param api_secret: The api_secret of this Tenant.  # noqa: E501
        :type: Str
        """


        self._api_secret = api_secret

    @property
    def audit_logs(self):
        """Gets the audit_logs of this Tenant.  # noqa: E501


        :return: The audit_logs of this Tenant.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this Tenant.


        :param audit_logs: The audit_logs of this Tenant.  # noqa: E501
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
        if not isinstance(other, Tenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other