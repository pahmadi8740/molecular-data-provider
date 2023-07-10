# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.model_property import ModelProperty
from openapi_server import util

from openapi_server.models.model_property import ModelProperty  # noqa: E501

class MoleProQuery(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, collection_id=None, controls=None):  # noqa: E501
        """MoleProQuery - a model defined in OpenAPI

        :param name: The name of this MoleProQuery.  # noqa: E501
        :type name: str
        :param collection_id: The collection_id of this MoleProQuery.  # noqa: E501
        :type collection_id: str
        :param controls: The controls of this MoleProQuery.  # noqa: E501
        :type controls: List[ModelProperty]
        """
        self.openapi_types = {
            'name': str,
            'collection_id': str,
            'controls': List[ModelProperty]
        }

        self.attribute_map = {
            'name': 'name',
            'collection_id': 'collection_id',
            'controls': 'controls'
        }

        self._name = name
        self._collection_id = collection_id
        self._controls = controls

    @classmethod
    def from_dict(cls, dikt) -> 'MoleProQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The mole_pro_query of this MoleProQuery.  # noqa: E501
        :rtype: MoleProQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this MoleProQuery.

        Name of the transformer that will be executed.  # noqa: E501

        :return: The name of this MoleProQuery.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MoleProQuery.

        Name of the transformer that will be executed.  # noqa: E501

        :param name: The name of this MoleProQuery.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def collection_id(self):
        """Gets the collection_id of this MoleProQuery.

        Id of the gene list that will be transformed. Required for all transformers except producers.  # noqa: E501

        :return: The collection_id of this MoleProQuery.
        :rtype: str
        """
        return self._collection_id

    @collection_id.setter
    def collection_id(self, collection_id):
        """Sets the collection_id of this MoleProQuery.

        Id of the gene list that will be transformed. Required for all transformers except producers.  # noqa: E501

        :param collection_id: The collection_id of this MoleProQuery.
        :type collection_id: str
        """

        self._collection_id = collection_id

    @property
    def controls(self):
        """Gets the controls of this MoleProQuery.

        Values that control the behavior of the transformer. Names of the controls must match the names specified in the transformer's definition and values must match types (and possibly  allowed_values) specified in the transformer's definition.  # noqa: E501

        :return: The controls of this MoleProQuery.
        :rtype: List[ModelProperty]
        """
        return self._controls

    @controls.setter
    def controls(self, controls):
        """Sets the controls of this MoleProQuery.

        Values that control the behavior of the transformer. Names of the controls must match the names specified in the transformer's definition and values must match types (and possibly  allowed_values) specified in the transformer's definition.  # noqa: E501

        :param controls: The controls of this MoleProQuery.
        :type controls: List[ModelProperty]
        """
        if controls is None:
            raise ValueError("Invalid value for `controls`, must not be `None`")  # noqa: E501

        self._controls = controls
