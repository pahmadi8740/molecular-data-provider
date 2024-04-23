# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Parameter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, type=None, required=None, multivalued=None, default=None, example=None, allowed_values=None, allowed_range=None, suggested_values=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI

        :param name: The name of this Parameter.  # noqa: E501
        :type name: str
        :param type: The type of this Parameter.  # noqa: E501
        :type type: str
        :param required: The required of this Parameter.  # noqa: E501
        :type required: bool
        :param multivalued: The multivalued of this Parameter.  # noqa: E501
        :type multivalued: bool
        :param default: The default of this Parameter.  # noqa: E501
        :type default: str
        :param example: The example of this Parameter.  # noqa: E501
        :type example: str
        :param allowed_values: The allowed_values of this Parameter.  # noqa: E501
        :type allowed_values: List[str]
        :param allowed_range: The allowed_range of this Parameter.  # noqa: E501
        :type allowed_range: List[float]
        :param suggested_values: The suggested_values of this Parameter.  # noqa: E501
        :type suggested_values: str
        """
        self.openapi_types = {
            'name': str,
            'type': str,
            'required': bool,
            'multivalued': bool,
            'default': str,
            'example': str,
            'allowed_values': List[str],
            'allowed_range': List[float],
            'suggested_values': str
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'required': 'required',
            'multivalued': 'multivalued',
            'default': 'default',
            'example': 'example',
            'allowed_values': 'allowed_values',
            'allowed_range': 'allowed_range',
            'suggested_values': 'suggested_values'
        }

        self._name = name
        self._type = type
        self._required = required
        self._multivalued = multivalued
        self._default = default
        self._example = example
        self._allowed_values = allowed_values
        self._allowed_range = allowed_range
        self._suggested_values = suggested_values

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Parameter.

        Name of the parameter.  # noqa: E501

        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        Name of the parameter.  # noqa: E501

        :param name: The name of this Parameter.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Parameter.

        Type of the parameter, one of 'Boolean', 'int', 'double', 'string'.  # noqa: E501

        :return: The type of this Parameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.

        Type of the parameter, one of 'Boolean', 'int', 'double', 'string'.  # noqa: E501

        :param type: The type of this Parameter.
        :type type: str
        """
        allowed_values = ["Boolean", "int", "double", "string"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def required(self):
        """Gets the required of this Parameter.

        Indicates whether the parameter is required(default true).  # noqa: E501

        :return: The required of this Parameter.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Parameter.

        Indicates whether the parameter is required(default true).  # noqa: E501

        :param required: The required of this Parameter.
        :type required: bool
        """

        self._required = required

    @property
    def multivalued(self):
        """Gets the multivalued of this Parameter.

        Indicates whether multiple occurences of the parameter are allowed (default false).  # noqa: E501

        :return: The multivalued of this Parameter.
        :rtype: bool
        """
        return self._multivalued

    @multivalued.setter
    def multivalued(self, multivalued):
        """Sets the multivalued of this Parameter.

        Indicates whether multiple occurences of the parameter are allowed (default false).  # noqa: E501

        :param multivalued: The multivalued of this Parameter.
        :type multivalued: bool
        """

        self._multivalued = multivalued

    @property
    def default(self):
        """Gets the default of this Parameter.

        Default value of the parameter.  # noqa: E501

        :return: The default of this Parameter.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Parameter.

        Default value of the parameter.  # noqa: E501

        :param default: The default of this Parameter.
        :type default: str
        """

        self._default = default

    @property
    def example(self):
        """Gets the example of this Parameter.

        Example value of the parameter.  # noqa: E501

        :return: The example of this Parameter.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this Parameter.

        Example value of the parameter.  # noqa: E501

        :param example: The example of this Parameter.
        :type example: str
        """

        self._example = example

    @property
    def allowed_values(self):
        """Gets the allowed_values of this Parameter.

        Allowed values for the parameter.  # noqa: E501

        :return: The allowed_values of this Parameter.
        :rtype: List[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this Parameter.

        Allowed values for the parameter.  # noqa: E501

        :param allowed_values: The allowed_values of this Parameter.
        :type allowed_values: List[str]
        """

        self._allowed_values = allowed_values

    @property
    def allowed_range(self):
        """Gets the allowed_range of this Parameter.

        Allowed range for values of the parameter.  # noqa: E501

        :return: The allowed_range of this Parameter.
        :rtype: List[float]
        """
        return self._allowed_range

    @allowed_range.setter
    def allowed_range(self, allowed_range):
        """Sets the allowed_range of this Parameter.

        Allowed range for values of the parameter.  # noqa: E501

        :param allowed_range: The allowed_range of this Parameter.
        :type allowed_range: List[float]
        """

        self._allowed_range = allowed_range

    @property
    def suggested_values(self):
        """Gets the suggested_values of this Parameter.

        Suggested value range for the parameter.  # noqa: E501

        :return: The suggested_values of this Parameter.
        :rtype: str
        """
        return self._suggested_values

    @suggested_values.setter
    def suggested_values(self, suggested_values):
        """Sets the suggested_values of this Parameter.

        Suggested value range for the parameter.  # noqa: E501

        :param suggested_values: The suggested_values of this Parameter.
        :type suggested_values: str
        """

        self._suggested_values = suggested_values
