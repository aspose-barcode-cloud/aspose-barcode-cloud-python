# coding: utf-8

"""

    Copyright (c) 2023 Aspose.BarCode for Cloud

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

import six


class AustralianPostParams(object):
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
        "encoding_table": "CustomerInformationInterpretingType",
        "short_bar_height": "float",
    }

    attribute_map = {
        "encoding_table": "EncodingTable",
        "short_bar_height": "ShortBarHeight",
    }

    def __init__(self, encoding_table=None, short_bar_height=None):  # noqa: E501
        """AustralianPostParams - a model defined in Swagger"""  # noqa: E501

        self._encoding_table = None
        self._short_bar_height = None
        self.discriminator = None

        if encoding_table is not None:
            self.encoding_table = encoding_table
        if short_bar_height is not None:
            self.short_bar_height = short_bar_height

    @property
    def encoding_table(self):
        """Gets the encoding_table of this AustralianPostParams.  # noqa: E501

        Interpreting type for the Customer Information of AustralianPost, default to CustomerInformationInterpretingType.Other\"  # noqa: E501

        :return: The encoding_table of this AustralianPostParams.  # noqa: E501
        :rtype: CustomerInformationInterpretingType
        """
        return self._encoding_table

    @encoding_table.setter
    def encoding_table(self, encoding_table):
        """Sets the encoding_table of this AustralianPostParams.

        Interpreting type for the Customer Information of AustralianPost, default to CustomerInformationInterpretingType.Other\"  # noqa: E501

        :param encoding_table: The encoding_table of this AustralianPostParams.  # noqa: E501
        :type: CustomerInformationInterpretingType
        """

        self._encoding_table = encoding_table

    @property
    def short_bar_height(self):
        """Gets the short_bar_height of this AustralianPostParams.  # noqa: E501

        Short bar's height of AustralianPost barcode.  # noqa: E501

        :return: The short_bar_height of this AustralianPostParams.  # noqa: E501
        :rtype: float
        """
        return self._short_bar_height

    @short_bar_height.setter
    def short_bar_height(self, short_bar_height):
        """Sets the short_bar_height of this AustralianPostParams.

        Short bar's height of AustralianPost barcode.  # noqa: E501

        :param short_bar_height: The short_bar_height of this AustralianPostParams.  # noqa: E501
        :type: float
        """

        self._short_bar_height = short_bar_height

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
        if issubclass(AustralianPostParams, dict):
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
        if not isinstance(other, AustralianPostParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
