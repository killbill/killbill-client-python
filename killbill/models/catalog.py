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

from killbill.models.price_list import PriceList  # noqa: F401,E501
from killbill.models.product import Product  # noqa: F401,E501
from killbill.models.unit import Unit  # noqa: F401,E501


class Catalog(object):
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
        'effective_date': 'datetime',
        'currencies': 'list[str]',
        'units': 'list[Unit]',
        'products': 'list[Product]',
        'price_lists': 'list[PriceList]'
    }

    attribute_map = {
        'name': 'name',
        'effective_date': 'effectiveDate',
        'currencies': 'currencies',
        'units': 'units',
        'products': 'products',
        'price_lists': 'priceLists'
    }

    def __init__(self, name=None, effective_date=None, currencies=None, units=None, products=None, price_lists=None):  # noqa: E501
        """Catalog - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._effective_date = None
        self._currencies = None
        self._units = None
        self._products = None
        self._price_lists = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if effective_date is not None:
            self.effective_date = effective_date
        if currencies is not None:
            self.currencies = currencies
        if units is not None:
            self.units = units
        if products is not None:
            self.products = products
        if price_lists is not None:
            self.price_lists = price_lists

    @property
    def name(self):
        """Gets the name of this Catalog.  # noqa: E501


        :return: The name of this Catalog.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Catalog.


        :param name: The name of this Catalog.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def effective_date(self):
        """Gets the effective_date of this Catalog.  # noqa: E501


        :return: The effective_date of this Catalog.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this Catalog.


        :param effective_date: The effective_date of this Catalog.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def currencies(self):
        """Gets the currencies of this Catalog.  # noqa: E501


        :return: The currencies of this Catalog.  # noqa: E501
        :rtype: list[str]
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """Sets the currencies of this Catalog.


        :param currencies: The currencies of this Catalog.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWD", "BTC"]  # noqa: E501
        if not set(currencies).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `currencies` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(currencies) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._currencies = currencies

    @property
    def units(self):
        """Gets the units of this Catalog.  # noqa: E501


        :return: The units of this Catalog.  # noqa: E501
        :rtype: list[Unit]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Catalog.


        :param units: The units of this Catalog.  # noqa: E501
        :type: list[Unit]
        """

        self._units = units

    @property
    def products(self):
        """Gets the products of this Catalog.  # noqa: E501


        :return: The products of this Catalog.  # noqa: E501
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Catalog.


        :param products: The products of this Catalog.  # noqa: E501
        :type: list[Product]
        """

        self._products = products

    @property
    def price_lists(self):
        """Gets the price_lists of this Catalog.  # noqa: E501


        :return: The price_lists of this Catalog.  # noqa: E501
        :rtype: list[PriceList]
        """
        return self._price_lists

    @price_lists.setter
    def price_lists(self, price_lists):
        """Sets the price_lists of this Catalog.


        :param price_lists: The price_lists of this Catalog.  # noqa: E501
        :type: list[PriceList]
        """

        self._price_lists = price_lists

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
        if not isinstance(other, Catalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
