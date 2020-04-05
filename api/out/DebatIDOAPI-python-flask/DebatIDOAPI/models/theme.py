# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from DebatIDOAPI.models.base_model_ import Model
from DebatIDOAPI import util


class Theme(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, title=None):  # noqa: E501
        """Theme - a model defined in OpenAPI

        :param id: The id of this Theme.  # noqa: E501
        :type id: int
        :param title: The title of this Theme.  # noqa: E501
        :type title: str
        """
        self.openapi_types = {
            'id': int,
            'title': str
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title'
        }

        self._id = id
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'Theme':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The theme of this Theme.  # noqa: E501
        :rtype: Theme
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Theme.


        :return: The id of this Theme.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Theme.


        :param id: The id of this Theme.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this Theme.


        :return: The title of this Theme.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Theme.


        :param title: The title of this Theme.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title
