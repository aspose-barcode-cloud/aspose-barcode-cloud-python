# coding: utf-8

"""

    Copyright (c) 2022 Aspose.BarCode for Cloud

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


class CaptionParams(object):
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
        "text": "str",
        "alignment": "TextAlignment",
        "color": "str",
        "visible": "bool",
        "font": "FontParams",
        "padding": "Padding",
        "no_wrap": "bool",
    }

    attribute_map = {
        "text": "Text",
        "alignment": "Alignment",
        "color": "Color",
        "visible": "Visible",
        "font": "Font",
        "padding": "Padding",
        "no_wrap": "NoWrap",
    }

    def __init__(
        self, text=None, alignment=None, color=None, visible=None, font=None, padding=None, no_wrap=None
    ):  # noqa: E501
        """CaptionParams - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._alignment = None
        self._color = None
        self._visible = None
        self._font = None
        self._padding = None
        self._no_wrap = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if alignment is not None:
            self.alignment = alignment
        if color is not None:
            self.color = color
        if visible is not None:
            self.visible = visible
        if font is not None:
            self.font = font
        if padding is not None:
            self.padding = padding
        if no_wrap is not None:
            self.no_wrap = no_wrap

    @property
    def text(self):
        """Gets the text of this CaptionParams.  # noqa: E501

        Caption text.  # noqa: E501

        :return: The text of this CaptionParams.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CaptionParams.

        Caption text.  # noqa: E501

        :param text: The text of this CaptionParams.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def alignment(self):
        """Gets the alignment of this CaptionParams.  # noqa: E501

        Text alignment.  # noqa: E501

        :return: The alignment of this CaptionParams.  # noqa: E501
        :rtype: TextAlignment
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this CaptionParams.

        Text alignment.  # noqa: E501

        :param alignment: The alignment of this CaptionParams.  # noqa: E501
        :type: TextAlignment
        """

        self._alignment = alignment

    @property
    def color(self):
        """Gets the color of this CaptionParams.  # noqa: E501

        Text color.  # noqa: E501

        :return: The color of this CaptionParams.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CaptionParams.

        Text color.  # noqa: E501

        :param color: The color of this CaptionParams.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def visible(self):
        """Gets the visible of this CaptionParams.  # noqa: E501

        Is caption visible.  # noqa: E501

        :return: The visible of this CaptionParams.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this CaptionParams.

        Is caption visible.  # noqa: E501

        :param visible: The visible of this CaptionParams.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def font(self):
        """Gets the font of this CaptionParams.  # noqa: E501

        Font.  # noqa: E501

        :return: The font of this CaptionParams.  # noqa: E501
        :rtype: FontParams
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this CaptionParams.

        Font.  # noqa: E501

        :param font: The font of this CaptionParams.  # noqa: E501
        :type: FontParams
        """

        self._font = font

    @property
    def padding(self):
        """Gets the padding of this CaptionParams.  # noqa: E501

        Padding.  # noqa: E501

        :return: The padding of this CaptionParams.  # noqa: E501
        :rtype: Padding
        """
        return self._padding

    @padding.setter
    def padding(self, padding):
        """Sets the padding of this CaptionParams.

        Padding.  # noqa: E501

        :param padding: The padding of this CaptionParams.  # noqa: E501
        :type: Padding
        """

        self._padding = padding

    @property
    def no_wrap(self):
        """Gets the no_wrap of this CaptionParams.  # noqa: E501

        Specify word wraps (line breaks) within text. Default value: false.  # noqa: E501

        :return: The no_wrap of this CaptionParams.  # noqa: E501
        :rtype: bool
        """
        return self._no_wrap

    @no_wrap.setter
    def no_wrap(self, no_wrap):
        """Sets the no_wrap of this CaptionParams.

        Specify word wraps (line breaks) within text. Default value: false.  # noqa: E501

        :param no_wrap: The no_wrap of this CaptionParams.  # noqa: E501
        :type: bool
        """

        self._no_wrap = no_wrap

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
        if issubclass(CaptionParams, dict):
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
        if not isinstance(other, CaptionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
