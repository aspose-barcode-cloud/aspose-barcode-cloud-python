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


class DataMatrixParams(object):
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
        "text_encoding": "str",
        "columns": "int",
        "data_matrix_ecc": "DataMatrixEccType",
        "data_matrix_encode_mode": "DataMatrixEncodeMode",
        "rows": "int",
        "macro_characters": "MacroCharacter",
    }

    attribute_map = {
        "aspect_ratio": "AspectRatio",
        "text_encoding": "TextEncoding",
        "columns": "Columns",
        "data_matrix_ecc": "DataMatrixEcc",
        "data_matrix_encode_mode": "DataMatrixEncodeMode",
        "rows": "Rows",
        "macro_characters": "MacroCharacters",
    }

    def __init__(
        self,
        aspect_ratio=None,
        text_encoding=None,
        columns=None,
        data_matrix_ecc=None,
        data_matrix_encode_mode=None,
        rows=None,
        macro_characters=None,
    ):  # noqa: E501
        """DataMatrixParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._text_encoding = None
        self._columns = None
        self._data_matrix_ecc = None
        self._data_matrix_encode_mode = None
        self._rows = None
        self._macro_characters = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if text_encoding is not None:
            self.text_encoding = text_encoding
        if columns is not None:
            self.columns = columns
        if data_matrix_ecc is not None:
            self.data_matrix_ecc = data_matrix_ecc
        if data_matrix_encode_mode is not None:
            self.data_matrix_encode_mode = data_matrix_encode_mode
        if rows is not None:
            self.rows = rows
        if macro_characters is not None:
            self.macro_characters = macro_characters

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this DataMatrixParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module  # noqa: E501

        :return: The aspect_ratio of this DataMatrixParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this DataMatrixParams.

        Height/Width ratio of 2D BarCode module  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this DataMatrixParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def text_encoding(self):
        """Gets the text_encoding of this DataMatrixParams.  # noqa: E501

        Encoding of codetext.  # noqa: E501

        :return: The text_encoding of this DataMatrixParams.  # noqa: E501
        :rtype: str
        """
        return self._text_encoding

    @text_encoding.setter
    def text_encoding(self, text_encoding):
        """Sets the text_encoding of this DataMatrixParams.

        Encoding of codetext.  # noqa: E501

        :param text_encoding: The text_encoding of this DataMatrixParams.  # noqa: E501
        :type: str
        """

        self._text_encoding = text_encoding

    @property
    def columns(self):
        """Gets the columns of this DataMatrixParams.  # noqa: E501

        DEPRECATED: Will be replaced with 'DataMatrix.Version' in the next release  Columns count.  # noqa: E501

        :return: The columns of this DataMatrixParams.  # noqa: E501
        :rtype: int
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this DataMatrixParams.

        DEPRECATED: Will be replaced with 'DataMatrix.Version' in the next release  Columns count.  # noqa: E501

        :param columns: The columns of this DataMatrixParams.  # noqa: E501
        :type: int
        """
        warnings.warn(
            "Property 'columns' is deprecated. Will be replaced with 'DataMatrix.Version' in the next release  Columns count.",  # noqa: E501
            category=DeprecationWarning,
        )

        self._columns = columns

    @property
    def data_matrix_ecc(self):
        """Gets the data_matrix_ecc of this DataMatrixParams.  # noqa: E501

        Datamatrix ECC type. Default value: DataMatrixEccType.Ecc200.  # noqa: E501

        :return: The data_matrix_ecc of this DataMatrixParams.  # noqa: E501
        :rtype: DataMatrixEccType
        """
        return self._data_matrix_ecc

    @data_matrix_ecc.setter
    def data_matrix_ecc(self, data_matrix_ecc):
        """Sets the data_matrix_ecc of this DataMatrixParams.

        Datamatrix ECC type. Default value: DataMatrixEccType.Ecc200.  # noqa: E501

        :param data_matrix_ecc: The data_matrix_ecc of this DataMatrixParams.  # noqa: E501
        :type: DataMatrixEccType
        """

        self._data_matrix_ecc = data_matrix_ecc

    @property
    def data_matrix_encode_mode(self):
        """Gets the data_matrix_encode_mode of this DataMatrixParams.  # noqa: E501

        Encode mode of Datamatrix barcode. Default value: DataMatrixEncodeMode.Auto.  # noqa: E501

        :return: The data_matrix_encode_mode of this DataMatrixParams.  # noqa: E501
        :rtype: DataMatrixEncodeMode
        """
        return self._data_matrix_encode_mode

    @data_matrix_encode_mode.setter
    def data_matrix_encode_mode(self, data_matrix_encode_mode):
        """Sets the data_matrix_encode_mode of this DataMatrixParams.

        Encode mode of Datamatrix barcode. Default value: DataMatrixEncodeMode.Auto.  # noqa: E501

        :param data_matrix_encode_mode: The data_matrix_encode_mode of this DataMatrixParams.  # noqa: E501
        :type: DataMatrixEncodeMode
        """

        self._data_matrix_encode_mode = data_matrix_encode_mode

    @property
    def rows(self):
        """Gets the rows of this DataMatrixParams.  # noqa: E501

        DEPRECATED: Will be replaced with 'DataMatrix.Version' in the next release  Rows count.  # noqa: E501

        :return: The rows of this DataMatrixParams.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this DataMatrixParams.

        DEPRECATED: Will be replaced with 'DataMatrix.Version' in the next release  Rows count.  # noqa: E501

        :param rows: The rows of this DataMatrixParams.  # noqa: E501
        :type: int
        """
        warnings.warn(
            "Property 'rows' is deprecated. Will be replaced with 'DataMatrix.Version' in the next release  Rows count.",  # noqa: E501
            category=DeprecationWarning,
        )

        self._rows = rows

    @property
    def macro_characters(self):
        """Gets the macro_characters of this DataMatrixParams.  # noqa: E501

        Macro Characters 05 and 06 values are used to obtain more compact encoding in special modes. Can be used only with DataMatrixEccType.Ecc200 or DataMatrixEccType.EccAuto. Cannot be used with EncodeTypes.GS1DataMatrix Default value: MacroCharacters.None.  # noqa: E501

        :return: The macro_characters of this DataMatrixParams.  # noqa: E501
        :rtype: MacroCharacter
        """
        return self._macro_characters

    @macro_characters.setter
    def macro_characters(self, macro_characters):
        """Sets the macro_characters of this DataMatrixParams.

        Macro Characters 05 and 06 values are used to obtain more compact encoding in special modes. Can be used only with DataMatrixEccType.Ecc200 or DataMatrixEccType.EccAuto. Cannot be used with EncodeTypes.GS1DataMatrix Default value: MacroCharacters.None.  # noqa: E501

        :param macro_characters: The macro_characters of this DataMatrixParams.  # noqa: E501
        :type: MacroCharacter
        """

        self._macro_characters = macro_characters

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
        if issubclass(DataMatrixParams, dict):
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
        if not isinstance(other, DataMatrixParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
