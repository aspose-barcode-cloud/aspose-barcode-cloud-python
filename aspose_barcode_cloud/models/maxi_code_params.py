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


class MaxiCodeParams(object):
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
    swagger_types = {"aspect_ratio": "float", "mode": "MaxiCodeMode", "encode_mode": "MaxiCodeEncodeMode"}

    attribute_map = {"aspect_ratio": "AspectRatio", "mode": "Mode", "encode_mode": "EncodeMode"}

    def __init__(self, aspect_ratio=None, mode=None, encode_mode=None):  # noqa: E501
        """MaxiCodeParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._mode = None
        self._encode_mode = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if mode is not None:
            self.mode = mode
        if encode_mode is not None:
            self.encode_mode = encode_mode

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this MaxiCodeParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :return: The aspect_ratio of this MaxiCodeParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this MaxiCodeParams.

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this MaxiCodeParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def mode(self):
        """Gets the mode of this MaxiCodeParams.  # noqa: E501

        Mode for MaxiCode barcodes.  # noqa: E501

        :return: The mode of this MaxiCodeParams.  # noqa: E501
        :rtype: MaxiCodeMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this MaxiCodeParams.

        Mode for MaxiCode barcodes.  # noqa: E501

        :param mode: The mode of this MaxiCodeParams.  # noqa: E501
        :type: MaxiCodeMode
        """

        self._mode = mode

    @property
    def encode_mode(self):
        """Gets the encode_mode of this MaxiCodeParams.  # noqa: E501

        Encoding mode for MaxiCode barcodes.  # noqa: E501

        :return: The encode_mode of this MaxiCodeParams.  # noqa: E501
        :rtype: MaxiCodeEncodeMode
        """
        return self._encode_mode

    @encode_mode.setter
    def encode_mode(self, encode_mode):
        """Sets the encode_mode of this MaxiCodeParams.

        Encoding mode for MaxiCode barcodes.  # noqa: E501

        :param encode_mode: The encode_mode of this MaxiCodeParams.  # noqa: E501
        :type: MaxiCodeEncodeMode
        """

        self._encode_mode = encode_mode

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
        if issubclass(MaxiCodeParams, dict):
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
        if not isinstance(other, MaxiCodeParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
