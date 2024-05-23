# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.attribute_constraint import AttributeConstraint
from openapi_server import util

from openapi_server.models.attribute_constraint import AttributeConstraint  # noqa: E501

class QNode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ids=None, categories=None, set_interpretation=None, member_ids=None, constraints=[]):  # noqa: E501
        """QNode - a model defined in OpenAPI

        :param ids: The ids of this QNode.  # noqa: E501
        :type ids: List[str]
        :param categories: The categories of this QNode.  # noqa: E501
        :type categories: List[str]
        :param set_interpretation: The set_interpretation of this QNode.  # noqa: E501
        :type set_interpretation: str
        :param member_ids: The member_ids of this QNode.  # noqa: E501
        :type member_ids: List[str]
        :param constraints: The constraints of this QNode.  # noqa: E501
        :type constraints: List[AttributeConstraint]
        """
        self.openapi_types = {
            'ids': List[str],
            'categories': List[str],
            'set_interpretation': str,
            'member_ids': List[str],
            'constraints': List[AttributeConstraint]
        }

        self.attribute_map = {
            'ids': 'ids',
            'categories': 'categories',
            'set_interpretation': 'set_interpretation',
            'member_ids': 'member_ids',
            'constraints': 'constraints'
        }

        self._ids = ids
        self._categories = categories
        self._set_interpretation = set_interpretation
        self._member_ids = member_ids
        self._constraints = constraints

    @classmethod
    def from_dict(cls, dikt) -> 'QNode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QNode of this QNode.  # noqa: E501
        :rtype: QNode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self):
        """Gets the ids of this QNode.

        A CURIE identifier (or list of identifiers) for this node.  The 'ids' field will hold a list of CURIEs only in the case of a BATCH set_interpretation, where each CURIE is queried  separately. If a list of queried CURIEs is to be considered as a   set (as under a MANY or ALL set_interpretation), the 'ids' field  will hold a single id representing this set, and the individual members  of this set will be captured in a separate 'member_ids' field.  Note that the set id MUST be created as a UUID by the system that  defines the queried set, using a centralized nodenorm service.  Note also that downstream systems MUST re-use the original set UUID  in the messages they create/send, which will facilitate merging or  caching operations.  # noqa: E501

        :return: The ids of this QNode.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this QNode.

        A CURIE identifier (or list of identifiers) for this node.  The 'ids' field will hold a list of CURIEs only in the case of a BATCH set_interpretation, where each CURIE is queried  separately. If a list of queried CURIEs is to be considered as a   set (as under a MANY or ALL set_interpretation), the 'ids' field  will hold a single id representing this set, and the individual members  of this set will be captured in a separate 'member_ids' field.  Note that the set id MUST be created as a UUID by the system that  defines the queried set, using a centralized nodenorm service.  Note also that downstream systems MUST re-use the original set UUID  in the messages they create/send, which will facilitate merging or  caching operations.  # noqa: E501

        :param ids: The ids of this QNode.
        :type ids: List[str]
        """
        if ids is not None and len(ids) < 1:
            raise ValueError("Invalid value for `ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ids = ids

    @property
    def categories(self):
        """Gets the categories of this QNode.

        These should be Biolink Model categories and are allowed to be of type 'abstract' or 'mixin' (only in QGraphs!). Use of 'deprecated' categories should be avoided.  # noqa: E501

        :return: The categories of this QNode.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this QNode.

        These should be Biolink Model categories and are allowed to be of type 'abstract' or 'mixin' (only in QGraphs!). Use of 'deprecated' categories should be avoided.  # noqa: E501

        :param categories: The categories of this QNode.
        :type categories: List[str]
        """
        if categories is not None and len(categories) < 1:
            raise ValueError("Invalid value for `categories`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._categories = categories

    @property
    def set_interpretation(self):
        """Gets the set_interpretation of this QNode.

        Indicates how multiple CURIEs in the ids property MUST be interpreted. BATCH indicates that the query is intended to be a batch query and each CURIE is treated independently. ALL means that all specified CURIES MUST appear in each Result. MANY means that member CURIEs MUST form one or more sets in the Results, and sets with more members are generally considered more desirable that sets with fewer members. If this property is missing or null, the default is BATCH.  # noqa: E501

        :return: The set_interpretation of this QNode.
        :rtype: str
        """
        return self._set_interpretation

    @set_interpretation.setter
    def set_interpretation(self, set_interpretation):
        """Sets the set_interpretation of this QNode.

        Indicates how multiple CURIEs in the ids property MUST be interpreted. BATCH indicates that the query is intended to be a batch query and each CURIE is treated independently. ALL means that all specified CURIES MUST appear in each Result. MANY means that member CURIEs MUST form one or more sets in the Results, and sets with more members are generally considered more desirable that sets with fewer members. If this property is missing or null, the default is BATCH.  # noqa: E501

        :param set_interpretation: The set_interpretation of this QNode.
        :type set_interpretation: str
        """
        allowed_values = [None,"BATCH", "ALL", "MANY"]  # noqa: E501
        if set_interpretation not in allowed_values:
            raise ValueError(
                "Invalid value for `set_interpretation` ({0}), must be one of {1}"
                .format(set_interpretation, allowed_values)
            )

        self._set_interpretation = set_interpretation

    @property
    def member_ids(self):
        """Gets the member_ids of this QNode.

        A list of CURIE identifiers for members of a queried set. This  field MUST be populated under a set_interpretation of MANY or ALL, when the 'ids' field holds a UUID representing the set  itself. This field MUST NOT be used under a set_interpretation  of BATCH.  # noqa: E501

        :return: The member_ids of this QNode.
        :rtype: List[str]
        """
        return self._member_ids

    @member_ids.setter
    def member_ids(self, member_ids):
        """Sets the member_ids of this QNode.

        A list of CURIE identifiers for members of a queried set. This  field MUST be populated under a set_interpretation of MANY or ALL, when the 'ids' field holds a UUID representing the set  itself. This field MUST NOT be used under a set_interpretation  of BATCH.  # noqa: E501

        :param member_ids: The member_ids of this QNode.
        :type member_ids: List[str]
        """

        self._member_ids = member_ids

    @property
    def constraints(self):
        """Gets the constraints of this QNode.

        A list of constraints applied to a query node. If there are multiple items, they must all be true (equivalent to AND)  # noqa: E501

        :return: The constraints of this QNode.
        :rtype: List[AttributeConstraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this QNode.

        A list of constraints applied to a query node. If there are multiple items, they must all be true (equivalent to AND)  # noqa: E501

        :param constraints: The constraints of this QNode.
        :type constraints: List[AttributeConstraint]
        """

        self._constraints = constraints