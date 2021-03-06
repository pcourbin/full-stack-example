# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from SPOTAPI.models.base_model_ import Model
from SPOTAPI.models.protagonist import Protagonist
from SPOTAPI.models.reference import Reference
from SPOTAPI import util

from SPOTAPI.models.protagonist import Protagonist  # noqa: E501
from SPOTAPI.models.reference import Reference  # noqa: E501

class ReferenceAuthor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, reference_id=None, reference=None, author_id=None, author=None):  # noqa: E501
        """ReferenceAuthor - a model defined in OpenAPI

        :param reference_id: The reference_id of this ReferenceAuthor.  # noqa: E501
        :type reference_id: int
        :param reference: The reference of this ReferenceAuthor.  # noqa: E501
        :type reference: Reference
        :param author_id: The author_id of this ReferenceAuthor.  # noqa: E501
        :type author_id: int
        :param author: The author of this ReferenceAuthor.  # noqa: E501
        :type author: Protagonist
        """
        self.openapi_types = {
            'reference_id': int,
            'reference': Reference,
            'author_id': int,
            'author': Protagonist
        }

        self.attribute_map = {
            'reference_id': 'referenceID',
            'reference': 'reference',
            'author_id': 'authorID',
            'author': 'author'
        }

        self._reference_id = reference_id
        self._reference = reference
        self._author_id = author_id
        self._author = author

    @classmethod
    def from_dict(cls, dikt) -> 'ReferenceAuthor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The referenceAuthor of this ReferenceAuthor.  # noqa: E501
        :rtype: ReferenceAuthor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reference_id(self):
        """Gets the reference_id of this ReferenceAuthor.


        :return: The reference_id of this ReferenceAuthor.
        :rtype: int
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this ReferenceAuthor.


        :param reference_id: The reference_id of this ReferenceAuthor.
        :type reference_id: int
        """
        if reference_id is None:
            raise ValueError("Invalid value for `reference_id`, must not be `None`")  # noqa: E501

        self._reference_id = reference_id

    @property
    def reference(self):
        """Gets the reference of this ReferenceAuthor.


        :return: The reference of this ReferenceAuthor.
        :rtype: Reference
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ReferenceAuthor.


        :param reference: The reference of this ReferenceAuthor.
        :type reference: Reference
        """

        self._reference = reference

    @property
    def author_id(self):
        """Gets the author_id of this ReferenceAuthor.


        :return: The author_id of this ReferenceAuthor.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this ReferenceAuthor.


        :param author_id: The author_id of this ReferenceAuthor.
        :type author_id: int
        """
        if author_id is None:
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def author(self):
        """Gets the author of this ReferenceAuthor.


        :return: The author of this ReferenceAuthor.
        :rtype: Protagonist
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ReferenceAuthor.


        :param author: The author of this ReferenceAuthor.
        :type author: Protagonist
        """

        self._author = author
