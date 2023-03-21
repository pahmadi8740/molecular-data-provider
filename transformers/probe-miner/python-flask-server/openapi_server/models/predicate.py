# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.km_attribute import KmAttribute
from openapi_server import util

from openapi_server.models.km_attribute import KmAttribute  # noqa: E501

class Predicate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subject=None, predicate=None, inverse_predicate=None, object=None, source=None, relations=None, inverse_relations=None, count=None, attributes=None):  # noqa: E501
        """Predicate - a model defined in OpenAPI

        :param subject: The subject of this Predicate.  # noqa: E501
        :type subject: str
        :param predicate: The predicate of this Predicate.  # noqa: E501
        :type predicate: str
        :param inverse_predicate: The inverse_predicate of this Predicate.  # noqa: E501
        :type inverse_predicate: str
        :param object: The object of this Predicate.  # noqa: E501
        :type object: str
        :param source: The source of this Predicate.  # noqa: E501
        :type source: str
        :param relations: The relations of this Predicate.  # noqa: E501
        :type relations: List[str]
        :param inverse_relations: The inverse_relations of this Predicate.  # noqa: E501
        :type inverse_relations: List[str]
        :param count: The count of this Predicate.  # noqa: E501
        :type count: int
        :param attributes: The attributes of this Predicate.  # noqa: E501
        :type attributes: List[KmAttribute]
        """
        self.openapi_types = {
            'subject': str,
            'predicate': str,
            'inverse_predicate': str,
            'object': str,
            'source': str,
            'relations': List[str],
            'inverse_relations': List[str],
            'count': int,
            'attributes': List[KmAttribute]
        }

        self.attribute_map = {
            'subject': 'subject',
            'predicate': 'predicate',
            'inverse_predicate': 'inverse_predicate',
            'object': 'object',
            'source': 'source',
            'relations': 'relations',
            'inverse_relations': 'inverse_relations',
            'count': 'count',
            'attributes': 'attributes'
        }

        self._subject = subject
        self._predicate = predicate
        self._inverse_predicate = inverse_predicate
        self._object = object
        self._source = source
        self._relations = relations
        self._inverse_relations = inverse_relations
        self._count = count
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'Predicate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The predicate of this Predicate.  # noqa: E501
        :rtype: Predicate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subject(self):
        """Gets the subject of this Predicate.


        :return: The subject of this Predicate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Predicate.


        :param subject: The subject of this Predicate.
        :type subject: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def predicate(self):
        """Gets the predicate of this Predicate.


        :return: The predicate of this Predicate.
        :rtype: str
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this Predicate.


        :param predicate: The predicate of this Predicate.
        :type predicate: str
        """
        if predicate is None:
            raise ValueError("Invalid value for `predicate`, must not be `None`")  # noqa: E501

        self._predicate = predicate

    @property
    def inverse_predicate(self):
        """Gets the inverse_predicate of this Predicate.


        :return: The inverse_predicate of this Predicate.
        :rtype: str
        """
        return self._inverse_predicate

    @inverse_predicate.setter
    def inverse_predicate(self, inverse_predicate):
        """Sets the inverse_predicate of this Predicate.


        :param inverse_predicate: The inverse_predicate of this Predicate.
        :type inverse_predicate: str
        """
        if inverse_predicate is None:
            raise ValueError("Invalid value for `inverse_predicate`, must not be `None`")  # noqa: E501

        self._inverse_predicate = inverse_predicate

    @property
    def object(self):
        """Gets the object of this Predicate.


        :return: The object of this Predicate.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Predicate.


        :param object: The object of this Predicate.
        :type object: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501

        self._object = object

    @property
    def source(self):
        """Gets the source of this Predicate.

        Source of the relationship.  # noqa: E501

        :return: The source of this Predicate.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Predicate.

        Source of the relationship.  # noqa: E501

        :param source: The source of this Predicate.
        :type source: str
        """

        self._source = source

    @property
    def relations(self):
        """Gets the relations of this Predicate.

        Low-level relations from the underlying source.  # noqa: E501

        :return: The relations of this Predicate.
        :rtype: List[str]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this Predicate.

        Low-level relations from the underlying source.  # noqa: E501

        :param relations: The relations of this Predicate.
        :type relations: List[str]
        """

        self._relations = relations

    @property
    def inverse_relations(self):
        """Gets the inverse_relations of this Predicate.

        Inverse low-level relations from the underlying source.  # noqa: E501

        :return: The inverse_relations of this Predicate.
        :rtype: List[str]
        """
        return self._inverse_relations

    @inverse_relations.setter
    def inverse_relations(self, inverse_relations):
        """Sets the inverse_relations of this Predicate.

        Inverse low-level relations from the underlying source.  # noqa: E501

        :param inverse_relations: The inverse_relations of this Predicate.
        :type inverse_relations: List[str]
        """

        self._inverse_relations = inverse_relations

    @property
    def count(self):
        """Gets the count of this Predicate.

        Number of edge instances known to this knowledge source  # noqa: E501

        :return: The count of this Predicate.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Predicate.

        Number of edge instances known to this knowledge source  # noqa: E501

        :param count: The count of this Predicate.
        :type count: int
        """

        self._count = count

    @property
    def attributes(self):
        """Gets the attributes of this Predicate.


        :return: The attributes of this Predicate.
        :rtype: List[KmAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Predicate.


        :param attributes: The attributes of this Predicate.
        :type attributes: List[KmAttribute]
        """

        self._attributes = attributes
