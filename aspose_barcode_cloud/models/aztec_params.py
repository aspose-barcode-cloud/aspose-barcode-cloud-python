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
import warnings  # noqa: F401

import six


class AztecParams(object):
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
        "error_level": "int",
        "symbol_mode": "AztecSymbolMode",
        "text_encoding": "str",
    }

    attribute_map = {
        "aspect_ratio": "AspectRatio",
        "error_level": "ErrorLevel",
        "symbol_mode": "SymbolMode",
        "text_encoding": "TextEncoding",
    }

    def __init__(self, aspect_ratio=None, error_level=None, symbol_mode=None, text_encoding=None):  # noqa: E501
        """AztecParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._error_level = None
        self._symbol_mode = None
        self._text_encoding = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if error_level is not None:
            self.error_level = error_level
        if symbol_mode is not None:
            self.symbol_mode = symbol_mode
        if text_encoding is not None:
            self.text_encoding = text_encoding

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this AztecParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :return: The aspect_ratio of this AztecParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this AztecParams.

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this AztecParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def error_level(self):
        """Gets the error_level of this AztecParams.  # noqa: E501

        Level of error correction of Aztec types of barcode. Value should between 10 to 95.  # noqa: E501

        :return: The error_level of this AztecParams.  # noqa: E501
        :rtype: int
        """
        return self._error_level

    @error_level.setter
    def error_level(self, error_level):
        """Sets the error_level of this AztecParams.

        Level of error correction of Aztec types of barcode. Value should between 10 to 95.  # noqa: E501

        :param error_level: The error_level of this AztecParams.  # noqa: E501
        :type: int
        """

        self._error_level = error_level

    @property
    def symbol_mode(self):
        """Gets the symbol_mode of this AztecParams.  # noqa: E501

        Aztec Symbol mode. Default value: AztecSymbolMode.Auto.  # noqa: E501

        :return: The symbol_mode of this AztecParams.  # noqa: E501
        :rtype: AztecSymbolMode
        """
        return self._symbol_mode

    @symbol_mode.setter
    def symbol_mode(self, symbol_mode):
        """Sets the symbol_mode of this AztecParams.

        Aztec Symbol mode. Default value: AztecSymbolMode.Auto.  # noqa: E501

        :param symbol_mode: The symbol_mode of this AztecParams.  # noqa: E501
        :type: AztecSymbolMode
        """

        self._symbol_mode = symbol_mode

    @property
    def text_encoding(self):
        """Gets the text_encoding of this AztecParams.  # noqa: E501

        Sets the encoding of codetext.  # noqa: E501

        :return: The text_encoding of this AztecParams.  # noqa: E501
        :rtype: str
        """
        return self._text_encoding

    @text_encoding.setter
    def text_encoding(self, text_encoding):
        """Sets the text_encoding of this AztecParams.

        Sets the encoding of codetext.  # noqa: E501

        :param text_encoding: The text_encoding of this AztecParams.  # noqa: E501
        :type: str
        """

        self._text_encoding = text_encoding

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
        if issubclass(AztecParams, dict):
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
        if not isinstance(other, AztecParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
