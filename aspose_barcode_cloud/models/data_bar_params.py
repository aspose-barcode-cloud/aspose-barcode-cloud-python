# coding: utf-8

"""

    Copyright (c) 2024 Aspose.BarCode for Cloud

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""


import pprint
import re  # noqa: F401
import warnings  # noqa: F401

import six


class DataBarParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "aspect_ratio": "float",
        "columns": "int",
        "rows": "int",
        "is2_d_composite_component": "bool",
        "is_allow_only_gs1_encoding": "bool",
    }

    attribute_map = {
        "aspect_ratio": "AspectRatio",
        "columns": "Columns",
        "rows": "Rows",
        "is2_d_composite_component": "Is2DCompositeComponent",
        "is_allow_only_gs1_encoding": "IsAllowOnlyGS1Encoding",
    }

    def __init__(
        self,
        aspect_ratio=None,
        columns=None,
        rows=None,
        is2_d_composite_component=None,
        is_allow_only_gs1_encoding=None,
    ):  # noqa: E501
        """DataBarParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._columns = None
        self._rows = None
        self._is2_d_composite_component = None
        self._is_allow_only_gs1_encoding = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if columns is not None:
            self.columns = columns
        if rows is not None:
            self.rows = rows
        if is2_d_composite_component is not None:
            self.is2_d_composite_component = is2_d_composite_component
        if is_allow_only_gs1_encoding is not None:
            self.is_allow_only_gs1_encoding = is_allow_only_gs1_encoding

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this DataBarParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module. Used for DataBar stacked.  # noqa: E501

        :return: The aspect_ratio of this DataBarParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this DataBarParams.

        Height/Width ratio of 2D BarCode module. Used for DataBar stacked.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this DataBarParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def columns(self):
        """Gets the columns of this DataBarParams.  # noqa: E501

        Columns count.  # noqa: E501

        :return: The columns of this DataBarParams.  # noqa: E501
        :rtype: int
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this DataBarParams.

        Columns count.  # noqa: E501

        :param columns: The columns of this DataBarParams.  # noqa: E501
        :type: int
        """

        self._columns = columns

    @property
    def rows(self):
        """Gets the rows of this DataBarParams.  # noqa: E501

        Rows count.  # noqa: E501

        :return: The rows of this DataBarParams.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this DataBarParams.

        Rows count.  # noqa: E501

        :param rows: The rows of this DataBarParams.  # noqa: E501
        :type: int
        """

        self._rows = rows

    @property
    def is2_d_composite_component(self):
        """Gets the is2_d_composite_component of this DataBarParams.  # noqa: E501

        Enables flag of 2D composite component with DataBar barcode  # noqa: E501

        :return: The is2_d_composite_component of this DataBarParams.  # noqa: E501
        :rtype: bool
        """
        return self._is2_d_composite_component

    @is2_d_composite_component.setter
    def is2_d_composite_component(self, is2_d_composite_component):
        """Sets the is2_d_composite_component of this DataBarParams.

        Enables flag of 2D composite component with DataBar barcode  # noqa: E501

        :param is2_d_composite_component: The is2_d_composite_component of this DataBarParams.  # noqa: E501
        :type: bool
        """

        self._is2_d_composite_component = is2_d_composite_component

    @property
    def is_allow_only_gs1_encoding(self):
        """Gets the is_allow_only_gs1_encoding of this DataBarParams.  # noqa: E501

        If this flag is set, it allows only GS1 encoding standard for Databar barcode types  # noqa: E501

        :return: The is_allow_only_gs1_encoding of this DataBarParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_allow_only_gs1_encoding

    @is_allow_only_gs1_encoding.setter
    def is_allow_only_gs1_encoding(self, is_allow_only_gs1_encoding):
        """Sets the is_allow_only_gs1_encoding of this DataBarParams.

        If this flag is set, it allows only GS1 encoding standard for Databar barcode types  # noqa: E501

        :param is_allow_only_gs1_encoding: The is_allow_only_gs1_encoding of this DataBarParams.  # noqa: E501
        :type: bool
        """

        self._is_allow_only_gs1_encoding = is_allow_only_gs1_encoding

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(DataBarParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataBarParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
