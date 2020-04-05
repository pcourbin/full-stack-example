# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from DebatIDOAPI.models.base_model_ import Model
from DebatIDOAPI.models.quote import Quote
from DebatIDOAPI import util

from DebatIDOAPI.models.quote import Quote  # noqa: E501

class QuoteLink(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, quote_main_id=None, quote_main=None, quote_support_id=None, quote_support=None, type_id=None, type_title=None, date_update=None):  # noqa: E501
        """QuoteLink - a model defined in OpenAPI

        :param quote_main_id: The quote_main_id of this QuoteLink.  # noqa: E501
        :type quote_main_id: int
        :param quote_main: The quote_main of this QuoteLink.  # noqa: E501
        :type quote_main: Quote
        :param quote_support_id: The quote_support_id of this QuoteLink.  # noqa: E501
        :type quote_support_id: int
        :param quote_support: The quote_support of this QuoteLink.  # noqa: E501
        :type quote_support: Quote
        :param type_id: The type_id of this QuoteLink.  # noqa: E501
        :type type_id: int
        :param type_title: The type_title of this QuoteLink.  # noqa: E501
        :type type_title: str
        :param date_update: The date_update of this QuoteLink.  # noqa: E501
        :type date_update: str
        """
        self.openapi_types = {
            'quote_main_id': int,
            'quote_main': Quote,
            'quote_support_id': int,
            'quote_support': Quote,
            'type_id': int,
            'type_title': str,
            'date_update': str
        }

        self.attribute_map = {
            'quote_main_id': 'quoteMainID',
            'quote_main': 'quoteMain',
            'quote_support_id': 'quoteSupportID',
            'quote_support': 'quoteSupport',
            'type_id': 'typeID',
            'type_title': 'typeTitle',
            'date_update': 'dateUpdate'
        }

        self._quote_main_id = quote_main_id
        self._quote_main = quote_main
        self._quote_support_id = quote_support_id
        self._quote_support = quote_support
        self._type_id = type_id
        self._type_title = type_title
        self._date_update = date_update

    @classmethod
    def from_dict(cls, dikt) -> 'QuoteLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The quoteLink of this QuoteLink.  # noqa: E501
        :rtype: QuoteLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quote_main_id(self):
        """Gets the quote_main_id of this QuoteLink.


        :return: The quote_main_id of this QuoteLink.
        :rtype: int
        """
        return self._quote_main_id

    @quote_main_id.setter
    def quote_main_id(self, quote_main_id):
        """Sets the quote_main_id of this QuoteLink.


        :param quote_main_id: The quote_main_id of this QuoteLink.
        :type quote_main_id: int
        """
        if quote_main_id is None:
            raise ValueError("Invalid value for `quote_main_id`, must not be `None`")  # noqa: E501

        self._quote_main_id = quote_main_id

    @property
    def quote_main(self):
        """Gets the quote_main of this QuoteLink.


        :return: The quote_main of this QuoteLink.
        :rtype: Quote
        """
        return self._quote_main

    @quote_main.setter
    def quote_main(self, quote_main):
        """Sets the quote_main of this QuoteLink.


        :param quote_main: The quote_main of this QuoteLink.
        :type quote_main: Quote
        """

        self._quote_main = quote_main

    @property
    def quote_support_id(self):
        """Gets the quote_support_id of this QuoteLink.


        :return: The quote_support_id of this QuoteLink.
        :rtype: int
        """
        return self._quote_support_id

    @quote_support_id.setter
    def quote_support_id(self, quote_support_id):
        """Sets the quote_support_id of this QuoteLink.


        :param quote_support_id: The quote_support_id of this QuoteLink.
        :type quote_support_id: int
        """
        if quote_support_id is None:
            raise ValueError("Invalid value for `quote_support_id`, must not be `None`")  # noqa: E501

        self._quote_support_id = quote_support_id

    @property
    def quote_support(self):
        """Gets the quote_support of this QuoteLink.


        :return: The quote_support of this QuoteLink.
        :rtype: Quote
        """
        return self._quote_support

    @quote_support.setter
    def quote_support(self, quote_support):
        """Sets the quote_support of this QuoteLink.


        :param quote_support: The quote_support of this QuoteLink.
        :type quote_support: Quote
        """

        self._quote_support = quote_support

    @property
    def type_id(self):
        """Gets the type_id of this QuoteLink.


        :return: The type_id of this QuoteLink.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this QuoteLink.


        :param type_id: The type_id of this QuoteLink.
        :type type_id: int
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def type_title(self):
        """Gets the type_title of this QuoteLink.


        :return: The type_title of this QuoteLink.
        :rtype: str
        """
        return self._type_title

    @type_title.setter
    def type_title(self, type_title):
        """Sets the type_title of this QuoteLink.


        :param type_title: The type_title of this QuoteLink.
        :type type_title: str
        """

        self._type_title = type_title

    @property
    def date_update(self):
        """Gets the date_update of this QuoteLink.


        :return: The date_update of this QuoteLink.
        :rtype: str
        """
        return self._date_update

    @date_update.setter
    def date_update(self, date_update):
        """Sets the date_update of this QuoteLink.


        :param date_update: The date_update of this QuoteLink.
        :type date_update: str
        """

        self._date_update = date_update
