# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class OperationOverlayFisherExactTestParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, subject_qnode_key=None, object_qnode_key=None, virtual_relation_label=None, rel_edge_key=None):  # noqa: E501
        """OperationOverlayFisherExactTestParameters - a model defined in OpenAPI

        :param subject_qnode_key: The subject_qnode_key of this OperationOverlayFisherExactTestParameters.  # noqa: E501
        :type subject_qnode_key: str
        :param object_qnode_key: The object_qnode_key of this OperationOverlayFisherExactTestParameters.  # noqa: E501
        :type object_qnode_key: str
        :param virtual_relation_label: The virtual_relation_label of this OperationOverlayFisherExactTestParameters.  # noqa: E501
        :type virtual_relation_label: str
        :param rel_edge_key: The rel_edge_key of this OperationOverlayFisherExactTestParameters.  # noqa: E501
        :type rel_edge_key: str
        """
        self.openapi_types = {
            'subject_qnode_key': str,
            'object_qnode_key': str,
            'virtual_relation_label': str,
            'rel_edge_key': str
        }

        self.attribute_map = {
            'subject_qnode_key': 'subject_qnode_key',
            'object_qnode_key': 'object_qnode_key',
            'virtual_relation_label': 'virtual_relation_label',
            'rel_edge_key': 'rel_edge_key'
        }

        self._subject_qnode_key = subject_qnode_key
        self._object_qnode_key = object_qnode_key
        self._virtual_relation_label = virtual_relation_label
        self._rel_edge_key = rel_edge_key

    @classmethod
    def from_dict(cls, dikt) -> 'OperationOverlayFisherExactTestParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperationOverlayFisherExactTest_parameters of this OperationOverlayFisherExactTestParameters.  # noqa: E501
        :rtype: OperationOverlayFisherExactTestParameters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subject_qnode_key(self):
        """Gets the subject_qnode_key of this OperationOverlayFisherExactTestParameters.

        A specific subject query node id.  # noqa: E501

        :return: The subject_qnode_key of this OperationOverlayFisherExactTestParameters.
        :rtype: str
        """
        return self._subject_qnode_key

    @subject_qnode_key.setter
    def subject_qnode_key(self, subject_qnode_key):
        """Sets the subject_qnode_key of this OperationOverlayFisherExactTestParameters.

        A specific subject query node id.  # noqa: E501

        :param subject_qnode_key: The subject_qnode_key of this OperationOverlayFisherExactTestParameters.
        :type subject_qnode_key: str
        """
        if subject_qnode_key is None:
            raise ValueError("Invalid value for `subject_qnode_key`, must not be `None`")  # noqa: E501

        self._subject_qnode_key = subject_qnode_key

    @property
    def object_qnode_key(self):
        """Gets the object_qnode_key of this OperationOverlayFisherExactTestParameters.

        A specific object query node id.  # noqa: E501

        :return: The object_qnode_key of this OperationOverlayFisherExactTestParameters.
        :rtype: str
        """
        return self._object_qnode_key

    @object_qnode_key.setter
    def object_qnode_key(self, object_qnode_key):
        """Sets the object_qnode_key of this OperationOverlayFisherExactTestParameters.

        A specific object query node id.  # noqa: E501

        :param object_qnode_key: The object_qnode_key of this OperationOverlayFisherExactTestParameters.
        :type object_qnode_key: str
        """
        if object_qnode_key is None:
            raise ValueError("Invalid value for `object_qnode_key`, must not be `None`")  # noqa: E501

        self._object_qnode_key = object_qnode_key

    @property
    def virtual_relation_label(self):
        """Gets the virtual_relation_label of this OperationOverlayFisherExactTestParameters.

        An label to help identify the virtual edge.  # noqa: E501

        :return: The virtual_relation_label of this OperationOverlayFisherExactTestParameters.
        :rtype: str
        """
        return self._virtual_relation_label

    @virtual_relation_label.setter
    def virtual_relation_label(self, virtual_relation_label):
        """Sets the virtual_relation_label of this OperationOverlayFisherExactTestParameters.

        An label to help identify the virtual edge.  # noqa: E501

        :param virtual_relation_label: The virtual_relation_label of this OperationOverlayFisherExactTestParameters.
        :type virtual_relation_label: str
        """
        if virtual_relation_label is None:
            raise ValueError("Invalid value for `virtual_relation_label`, must not be `None`")  # noqa: E501

        self._virtual_relation_label = virtual_relation_label

    @property
    def rel_edge_key(self):
        """Gets the rel_edge_key of this OperationOverlayFisherExactTestParameters.

        A specific Qedge id connected to both subject nodes and object nodes in message KG (optional, otherwise all edges connected to both subject nodes and object nodes in message KG are considered).  # noqa: E501

        :return: The rel_edge_key of this OperationOverlayFisherExactTestParameters.
        :rtype: str
        """
        return self._rel_edge_key

    @rel_edge_key.setter
    def rel_edge_key(self, rel_edge_key):
        """Sets the rel_edge_key of this OperationOverlayFisherExactTestParameters.

        A specific Qedge id connected to both subject nodes and object nodes in message KG (optional, otherwise all edges connected to both subject nodes and object nodes in message KG are considered).  # noqa: E501

        :param rel_edge_key: The rel_edge_key of this OperationOverlayFisherExactTestParameters.
        :type rel_edge_key: str
        """

        self._rel_edge_key = rel_edge_key