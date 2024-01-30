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
        "encode_mode": "AztecEncodeMode",
        "eci_encoding": "ECIEncodings",
        "is_reader_initialization": "bool",
        "layers_count": "int",
    }

    attribute_map = {
        "aspect_ratio": "AspectRatio",
        "error_level": "ErrorLevel",
        "symbol_mode": "SymbolMode",
        "text_encoding": "TextEncoding",
        "encode_mode": "EncodeMode",
        "eci_encoding": "ECIEncoding",
        "is_reader_initialization": "IsReaderInitialization",
        "layers_count": "LayersCount",
    }

    def __init__(
        self,
        aspect_ratio=None,
        error_level=None,
        symbol_mode=None,
        text_encoding=None,
        encode_mode=None,
        eci_encoding=None,
        is_reader_initialization=None,
        layers_count=None,
    ):  # noqa: E501
        """AztecParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._error_level = None
        self._symbol_mode = None
        self._text_encoding = None
        self._encode_mode = None
        self._eci_encoding = None
        self._is_reader_initialization = None
        self._layers_count = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if error_level is not None:
            self.error_level = error_level
        if symbol_mode is not None:
            self.symbol_mode = symbol_mode
        if text_encoding is not None:
            self.text_encoding = text_encoding
        if encode_mode is not None:
            self.encode_mode = encode_mode
        if eci_encoding is not None:
            self.eci_encoding = eci_encoding
        if is_reader_initialization is not None:
            self.is_reader_initialization = is_reader_initialization
        if layers_count is not None:
            self.layers_count = layers_count

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

        DEPRECATED: This property is obsolete and will be removed in future releases. Unicode symbols detection and encoding will be processed in Auto mode with Extended Channel Interpretation charset designator. Using of own encodings requires manual CodeText encoding into byte[] array.  Sets the encoding of codetext.  # noqa: E501

        :return: The text_encoding of this AztecParams.  # noqa: E501
        :rtype: str
        """
        return self._text_encoding

    @text_encoding.setter
    def text_encoding(self, text_encoding):
        """Sets the text_encoding of this AztecParams.

        DEPRECATED: This property is obsolete and will be removed in future releases. Unicode symbols detection and encoding will be processed in Auto mode with Extended Channel Interpretation charset designator. Using of own encodings requires manual CodeText encoding into byte[] array.  Sets the encoding of codetext.  # noqa: E501

        :param text_encoding: The text_encoding of this AztecParams.  # noqa: E501
        :type: str
        """
        warnings.warn(
            "Property 'text_encoding' is deprecated. This property is obsolete and will be removed in future releases. Unicode symbols detection and encoding will be processed in Auto mode with Extended Channel Interpretation charset designator. Using of own encodings requires manual CodeText encoding into byte[] array.  Sets the encoding of codetext.",  # noqa: E501
            category=DeprecationWarning,
        )

        self._text_encoding = text_encoding

    @property
    def encode_mode(self):
        """Gets the encode_mode of this AztecParams.  # noqa: E501

        Encoding mode for Aztec barcodes. Default value: Auto  # noqa: E501

        :return: The encode_mode of this AztecParams.  # noqa: E501
        :rtype: AztecEncodeMode
        """
        return self._encode_mode

    @encode_mode.setter
    def encode_mode(self, encode_mode):
        """Sets the encode_mode of this AztecParams.

        Encoding mode for Aztec barcodes. Default value: Auto  # noqa: E501

        :param encode_mode: The encode_mode of this AztecParams.  # noqa: E501
        :type: AztecEncodeMode
        """

        self._encode_mode = encode_mode

    @property
    def eci_encoding(self):
        """Gets the eci_encoding of this AztecParams.  # noqa: E501

        Identifies ECI encoding. Used when AztecEncodeMode is Auto. Default value: ISO-8859-1.  # noqa: E501

        :return: The eci_encoding of this AztecParams.  # noqa: E501
        :rtype: ECIEncodings
        """
        return self._eci_encoding

    @eci_encoding.setter
    def eci_encoding(self, eci_encoding):
        """Sets the eci_encoding of this AztecParams.

        Identifies ECI encoding. Used when AztecEncodeMode is Auto. Default value: ISO-8859-1.  # noqa: E501

        :param eci_encoding: The eci_encoding of this AztecParams.  # noqa: E501
        :type: ECIEncodings
        """

        self._eci_encoding = eci_encoding

    @property
    def is_reader_initialization(self):
        """Gets the is_reader_initialization of this AztecParams.  # noqa: E501

        Used to instruct the reader to interpret the data contained within the symbol as programming for reader initialization.  # noqa: E501

        :return: The is_reader_initialization of this AztecParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_reader_initialization

    @is_reader_initialization.setter
    def is_reader_initialization(self, is_reader_initialization):
        """Sets the is_reader_initialization of this AztecParams.

        Used to instruct the reader to interpret the data contained within the symbol as programming for reader initialization.  # noqa: E501

        :param is_reader_initialization: The is_reader_initialization of this AztecParams.  # noqa: E501
        :type: bool
        """

        self._is_reader_initialization = is_reader_initialization

    @property
    def layers_count(self):
        """Gets the layers_count of this AztecParams.  # noqa: E501

        Gets or sets layers count of Aztec symbol. Layers count should be in range from 1 to 3 for Compact mode and in range from 1 to 32 for Full Range mode. Default value: 0 (auto).  # noqa: E501

        :return: The layers_count of this AztecParams.  # noqa: E501
        :rtype: int
        """
        return self._layers_count

    @layers_count.setter
    def layers_count(self, layers_count):
        """Sets the layers_count of this AztecParams.

        Gets or sets layers count of Aztec symbol. Layers count should be in range from 1 to 3 for Compact mode and in range from 1 to 32 for Full Range mode. Default value: 0 (auto).  # noqa: E501

        :param layers_count: The layers_count of this AztecParams.  # noqa: E501
        :type: int
        """

        self._layers_count = layers_count

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
