# coding: utf-8

"""

    Copyright (c) 2021 Aspose.BarCode for Cloud

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


class DotCodeParams(object):
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
    swagger_types = {"aspect_ratio": "float", "dot_code_mask": "int"}

    attribute_map = {"aspect_ratio": "AspectRatio", "dot_code_mask": "DotCodeMask"}

    def __init__(self, aspect_ratio=None, dot_code_mask=None):  # noqa: E501
        """DotCodeParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._dot_code_mask = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if dot_code_mask is not None:
            self.dot_code_mask = dot_code_mask

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this DotCodeParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :return: The aspect_ratio of this DotCodeParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this DotCodeParams.

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this DotCodeParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def dot_code_mask(self):
        """Gets the dot_code_mask of this DotCodeParams.  # noqa: E501

        Mask of Dotcode barcode. Default value: -1.  # noqa: E501

        :return: The dot_code_mask of this DotCodeParams.  # noqa: E501
        :rtype: int
        """
        return self._dot_code_mask

    @dot_code_mask.setter
    def dot_code_mask(self, dot_code_mask):
        """Sets the dot_code_mask of this DotCodeParams.

        Mask of Dotcode barcode. Default value: -1.  # noqa: E501

        :param dot_code_mask: The dot_code_mask of this DotCodeParams.  # noqa: E501
        :type: int
        """

        self._dot_code_mask = dot_code_mask

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
        if issubclass(DotCodeParams, dict):
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
        if not isinstance(other, DotCodeParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
