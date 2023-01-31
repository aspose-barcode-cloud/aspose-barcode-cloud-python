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


class FontParams(object):
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
    swagger_types = {"family": "str", "size": "float", "style": "FontStyle"}

    attribute_map = {"family": "Family", "size": "Size", "style": "Style"}

    def __init__(self, family=None, size=None, style=None):  # noqa: E501
        """FontParams - a model defined in Swagger"""  # noqa: E501

        self._family = None
        self._size = None
        self._style = None
        self.discriminator = None

        if family is not None:
            self.family = family
        if size is not None:
            self.size = size
        if style is not None:
            self.style = style

    @property
    def family(self):
        """Gets the family of this FontParams.  # noqa: E501

        Font family.  # noqa: E501

        :return: The family of this FontParams.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this FontParams.

        Font family.  # noqa: E501

        :param family: The family of this FontParams.  # noqa: E501
        :type: str
        """

        self._family = family

    @property
    def size(self):
        """Gets the size of this FontParams.  # noqa: E501

        Font size in units.  # noqa: E501

        :return: The size of this FontParams.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FontParams.

        Font size in units.  # noqa: E501

        :param size: The size of this FontParams.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def style(self):
        """Gets the style of this FontParams.  # noqa: E501

        Font style.  # noqa: E501

        :return: The style of this FontParams.  # noqa: E501
        :rtype: FontStyle
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this FontParams.

        Font style.  # noqa: E501

        :param style: The style of this FontParams.  # noqa: E501
        :type: FontStyle
        """

        self._style = style

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
        if issubclass(FontParams, dict):
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
        if not isinstance(other, FontParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
