# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from DebatIDOAPI.models.base_model_ import Model
from DebatIDOAPI import util


class ReferenceModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, title: str=None, link: str=None, nature: str=None, _date: str=None, reliability: int=None):  # noqa: E501
        """ReferenceModel - a model defined in Swagger

        :param id: The id of this ReferenceModel.  # noqa: E501
        :type id: int
        :param name: The name of this ReferenceModel.  # noqa: E501
        :type name: str
        :param title: The title of this ReferenceModel.  # noqa: E501
        :type title: str
        :param link: The link of this ReferenceModel.  # noqa: E501
        :type link: str
        :param nature: The nature of this ReferenceModel.  # noqa: E501
        :type nature: str
        :param _date: The _date of this ReferenceModel.  # noqa: E501
        :type _date: str
        :param reliability: The reliability of this ReferenceModel.  # noqa: E501
        :type reliability: int
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'title': str,
            'link': str,
            'nature': str,
            '_date': str,
            'reliability': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'title': 'title',
            'link': 'link',
            'nature': 'nature',
            '_date': 'date',
            'reliability': 'reliability'
        }
        self._id = id
        self._name = name
        self._title = title
        self._link = link
        self._nature = nature
        self.__date = _date
        self._reliability = reliability

    @classmethod
    def from_dict(cls, dikt) -> 'ReferenceModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReferenceModel of this ReferenceModel.  # noqa: E501
        :rtype: ReferenceModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ReferenceModel.


        :return: The id of this ReferenceModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ReferenceModel.


        :param id: The id of this ReferenceModel.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this ReferenceModel.


        :return: The name of this ReferenceModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ReferenceModel.


        :param name: The name of this ReferenceModel.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self) -> str:
        """Gets the title of this ReferenceModel.


        :return: The title of this ReferenceModel.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this ReferenceModel.


        :param title: The title of this ReferenceModel.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def link(self) -> str:
        """Gets the link of this ReferenceModel.


        :return: The link of this ReferenceModel.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link: str):
        """Sets the link of this ReferenceModel.


        :param link: The link of this ReferenceModel.
        :type link: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def nature(self) -> str:
        """Gets the nature of this ReferenceModel.


        :return: The nature of this ReferenceModel.
        :rtype: str
        """
        return self._nature

    @nature.setter
    def nature(self, nature: str):
        """Sets the nature of this ReferenceModel.


        :param nature: The nature of this ReferenceModel.
        :type nature: str
        """
        if nature is None:
            raise ValueError("Invalid value for `nature`, must not be `None`")  # noqa: E501

        self._nature = nature

    @property
    def _date(self) -> str:
        """Gets the _date of this ReferenceModel.


        :return: The _date of this ReferenceModel.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this ReferenceModel.


        :param _date: The _date of this ReferenceModel.
        :type _date: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def reliability(self) -> int:
        """Gets the reliability of this ReferenceModel.


        :return: The reliability of this ReferenceModel.
        :rtype: int
        """
        return self._reliability

    @reliability.setter
    def reliability(self, reliability: int):
        """Sets the reliability of this ReferenceModel.


        :param reliability: The reliability of this ReferenceModel.
        :type reliability: int
        """
        if reliability is None:
            raise ValueError("Invalid value for `reliability`, must not be `None`")  # noqa: E501

        self._reliability = reliability