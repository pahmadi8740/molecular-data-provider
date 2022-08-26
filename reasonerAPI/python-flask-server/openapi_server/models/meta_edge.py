# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.meta_attribute import MetaAttribute
import re
from openapi_server import util

from openapi_server.models.meta_attribute import MetaAttribute  # noqa: E501
import re  # noqa: E501

class MetaEdge(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subject=None, predicate=None, object=None, knowledge_types=None, attributes=None):  # noqa: E501
        """MetaEdge - a model defined in OpenAPI

        :param subject: The subject of this MetaEdge.  # noqa: E501
        :type subject: str
        :param predicate: The predicate of this MetaEdge.  # noqa: E501
        :type predicate: str
        :param object: The object of this MetaEdge.  # noqa: E501
        :type object: str
        :param knowledge_types: The knowledge_types of this MetaEdge.  # noqa: E501
        :type knowledge_types: List[str]
        :param attributes: The attributes of this MetaEdge.  # noqa: E501
        :type attributes: List[MetaAttribute]
        """
        self.openapi_types = {
            'subject': str,
            'predicate': str,
            'object': str,
            'knowledge_types': List[str],
            'attributes': List[MetaAttribute]
        }

        self.attribute_map = {
            'subject': 'subject',
            'predicate': 'predicate',
            'object': 'object',
            'knowledge_types': 'knowledge_types',
            'attributes': 'attributes'
        }

        self._subject = subject
        self._predicate = predicate
        self._object = object
        self._knowledge_types = knowledge_types
        self._attributes = attributes

    @classmethod
    def from_dict(cls, dikt) -> 'MetaEdge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MetaEdge of this MetaEdge.  # noqa: E501
        :rtype: MetaEdge
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subject(self):
        """Gets the subject of this MetaEdge.

        Compact URI (CURIE) for a Biolink class, biolink:NamedThing or a child thereof. The CURIE must use the prefix 'biolink:' followed by the PascalCase class name.  # noqa: E501

        :return: The subject of this MetaEdge.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MetaEdge.

        Compact URI (CURIE) for a Biolink class, biolink:NamedThing or a child thereof. The CURIE must use the prefix 'biolink:' followed by the PascalCase class name.  # noqa: E501

        :param subject: The subject of this MetaEdge.
        :type subject: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501
        if subject is not None and not re.search(r'^biolink:[A-Z][a-zA-Z]*$', subject):  # noqa: E501
            raise ValueError("Invalid value for `subject`, must be a follow pattern or equal to `/^biolink:[A-Z][a-zA-Z]*$/`")  # noqa: E501

        self._subject = subject

    @property
    def predicate(self):
        """Gets the predicate of this MetaEdge.

        CURIE for a Biolink 'predicate' slot, taken from the Biolink slot ('is_a') hierarchy rooted in biolink:related_to (snake_case). This predicate defines the Biolink relationship between the subject and object nodes of a biolink:Association defining a knowledge graph edge.  # noqa: E501

        :return: The predicate of this MetaEdge.
        :rtype: str
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this MetaEdge.

        CURIE for a Biolink 'predicate' slot, taken from the Biolink slot ('is_a') hierarchy rooted in biolink:related_to (snake_case). This predicate defines the Biolink relationship between the subject and object nodes of a biolink:Association defining a knowledge graph edge.  # noqa: E501

        :param predicate: The predicate of this MetaEdge.
        :type predicate: str
        """
        if predicate is None:
            raise ValueError("Invalid value for `predicate`, must not be `None`")  # noqa: E501
        if predicate is not None and not re.search(r'^biolink:[a-z][a-z_]*$', predicate):  # noqa: E501
            raise ValueError("Invalid value for `predicate`, must be a follow pattern or equal to `/^biolink:[a-z][a-z_]*$/`")  # noqa: E501

        self._predicate = predicate

    @property
    def object(self):
        """Gets the object of this MetaEdge.

        Compact URI (CURIE) for a Biolink class, biolink:NamedThing or a child thereof. The CURIE must use the prefix 'biolink:' followed by the PascalCase class name.  # noqa: E501

        :return: The object of this MetaEdge.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this MetaEdge.

        Compact URI (CURIE) for a Biolink class, biolink:NamedThing or a child thereof. The CURIE must use the prefix 'biolink:' followed by the PascalCase class name.  # noqa: E501

        :param object: The object of this MetaEdge.
        :type object: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501
        if object is not None and not re.search(r'^biolink:[A-Z][a-zA-Z]*$', object):  # noqa: E501
            raise ValueError("Invalid value for `object`, must be a follow pattern or equal to `/^biolink:[A-Z][a-zA-Z]*$/`")  # noqa: E501

        self._object = object

    @property
    def knowledge_types(self):
        """Gets the knowledge_types of this MetaEdge.

        A list of knowledge_types that are supported by the service. If the knowledge_types is null, this means that only 'lookup' is supported. Currently allowed values are 'lookup' or 'inferred'.  # noqa: E501

        :return: The knowledge_types of this MetaEdge.
        :rtype: List[str]
        """
        return self._knowledge_types

    @knowledge_types.setter
    def knowledge_types(self, knowledge_types):
        """Sets the knowledge_types of this MetaEdge.

        A list of knowledge_types that are supported by the service. If the knowledge_types is null, this means that only 'lookup' is supported. Currently allowed values are 'lookup' or 'inferred'.  # noqa: E501

        :param knowledge_types: The knowledge_types of this MetaEdge.
        :type knowledge_types: List[str]
        """
        if knowledge_types is not None and len(knowledge_types) < 1:
            raise ValueError("Invalid value for `knowledge_types`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._knowledge_types = knowledge_types

    @property
    def attributes(self):
        """Gets the attributes of this MetaEdge.

        Edge attributes provided by this TRAPI web service.  # noqa: E501

        :return: The attributes of this MetaEdge.
        :rtype: List[MetaAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this MetaEdge.

        Edge attributes provided by this TRAPI web service.  # noqa: E501

        :param attributes: The attributes of this MetaEdge.
        :type attributes: List[MetaAttribute]
        """

        self._attributes = attributes