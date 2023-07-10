# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.attribute import Attribute
from openapi_server.models.compound_info_identifiers import CompoundInfoIdentifiers
from openapi_server.models.compound_info_structure import CompoundInfoStructure
from openapi_server.models.names import Names
from openapi_server import util

from openapi_server.models.attribute import Attribute  # noqa: E501
from openapi_server.models.compound_info_identifiers import CompoundInfoIdentifiers  # noqa: E501
from openapi_server.models.compound_info_structure import CompoundInfoStructure  # noqa: E501
from openapi_server.models.names import Names  # noqa: E501

class CompoundInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compound_id=None, identifiers=None, names_synonyms=None, structure=None, attributes=None, source=None):  # noqa: E501
        """CompoundInfo - a model defined in OpenAPI

        :param compound_id: The compound_id of this CompoundInfo.  # noqa: E501
        :type compound_id: str
        :param identifiers: The identifiers of this CompoundInfo.  # noqa: E501
        :type identifiers: CompoundInfoIdentifiers
        :param names_synonyms: The names_synonyms of this CompoundInfo.  # noqa: E501
        :type names_synonyms: List[Names]
        :param structure: The structure of this CompoundInfo.  # noqa: E501
        :type structure: CompoundInfoStructure
        :param attributes: The attributes of this CompoundInfo.  # noqa: E501
        :type attributes: List[Attribute]
        :param source: The source of this CompoundInfo.  # noqa: E501
        :type source: str
        """
        self.openapi_types = {
            'compound_id': str,
            'identifiers': CompoundInfoIdentifiers,
            'names_synonyms': List[Names],
            'structure': CompoundInfoStructure,
            'attributes': List[Attribute],
            'source': str
        }

        self.attribute_map = {
            'compound_id': 'compound_id',
            'identifiers': 'identifiers',
            'names_synonyms': 'names_synonyms',
            'structure': 'structure',
            'attributes': 'attributes',
            'source': 'source'
        }

        self._compound_id = compound_id
        self._identifiers = identifiers
        self._names_synonyms = names_synonyms
        self._structure = structure
        self._attributes = attributes
        self._source = source

    @classmethod
    def from_dict(cls, dikt) -> 'CompoundInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The compound_info of this CompoundInfo.  # noqa: E501
        :rtype: CompoundInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compound_id(self):
        """Gets the compound_id of this CompoundInfo.

        Ids of the compound.  # noqa: E501

        :return: The compound_id of this CompoundInfo.
        :rtype: str
        """
        return self._compound_id

    @compound_id.setter
    def compound_id(self, compound_id):
        """Sets the compound_id of this CompoundInfo.

        Ids of the compound.  # noqa: E501

        :param compound_id: The compound_id of this CompoundInfo.
        :type compound_id: str
        """
        if compound_id is None:
            raise ValueError("Invalid value for `compound_id`, must not be `None`")  # noqa: E501

        self._compound_id = compound_id

    @property
    def identifiers(self):
        """Gets the identifiers of this CompoundInfo.


        :return: The identifiers of this CompoundInfo.
        :rtype: CompoundInfoIdentifiers
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this CompoundInfo.


        :param identifiers: The identifiers of this CompoundInfo.
        :type identifiers: CompoundInfoIdentifiers
        """

        self._identifiers = identifiers

    @property
    def names_synonyms(self):
        """Gets the names_synonyms of this CompoundInfo.

        Compound names and synonyms.  # noqa: E501

        :return: The names_synonyms of this CompoundInfo.
        :rtype: List[Names]
        """
        return self._names_synonyms

    @names_synonyms.setter
    def names_synonyms(self, names_synonyms):
        """Sets the names_synonyms of this CompoundInfo.

        Compound names and synonyms.  # noqa: E501

        :param names_synonyms: The names_synonyms of this CompoundInfo.
        :type names_synonyms: List[Names]
        """

        self._names_synonyms = names_synonyms

    @property
    def structure(self):
        """Gets the structure of this CompoundInfo.


        :return: The structure of this CompoundInfo.
        :rtype: CompoundInfoStructure
        """
        return self._structure

    @structure.setter
    def structure(self, structure):
        """Sets the structure of this CompoundInfo.


        :param structure: The structure of this CompoundInfo.
        :type structure: CompoundInfoStructure
        """

        self._structure = structure

    @property
    def attributes(self):
        """Gets the attributes of this CompoundInfo.

        Additional information about the compound and provenance about compound-list membership.  # noqa: E501

        :return: The attributes of this CompoundInfo.
        :rtype: List[Attribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CompoundInfo.

        Additional information about the compound and provenance about compound-list membership.  # noqa: E501

        :param attributes: The attributes of this CompoundInfo.
        :type attributes: List[Attribute]
        """

        self._attributes = attributes

    @property
    def source(self):
        """Gets the source of this CompoundInfo.

        Name of a transformer that added compound to the compound list.  # noqa: E501

        :return: The source of this CompoundInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CompoundInfo.

        Name of a transformer that added compound to the compound list.  # noqa: E501

        :param source: The source of this CompoundInfo.
        :type source: str
        """

        self._source = source
