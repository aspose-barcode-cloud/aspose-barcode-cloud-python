# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401


class ECIEncodings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NONE = "NONE"
    ISO_8859_1 = "ISO_8859_1"
    ISO_8859_2 = "ISO_8859_2"
    ISO_8859_3 = "ISO_8859_3"
    ISO_8859_4 = "ISO_8859_4"
    ISO_8859_5 = "ISO_8859_5"
    ISO_8859_6 = "ISO_8859_6"
    ISO_8859_7 = "ISO_8859_7"
    ISO_8859_8 = "ISO_8859_8"
    ISO_8859_9 = "ISO_8859_9"
    ISO_8859_10 = "ISO_8859_10"
    ISO_8859_11 = "ISO_8859_11"
    ISO_8859_13 = "ISO_8859_13"
    ISO_8859_14 = "ISO_8859_14"
    ISO_8859_15 = "ISO_8859_15"
    ISO_8859_16 = "ISO_8859_16"
    SHIFT_JIS = "Shift_JIS"
    WIN1250 = "Win1250"
    WIN1251 = "Win1251"
    WIN1252 = "Win1252"
    WIN1256 = "Win1256"
    UTF16BE = "UTF16BE"
    UTF8 = "UTF8"
    US_ASCII = "US_ASCII"
    BIG5 = "Big5"
    GB18030 = "GB18030"
    EUC_KR = "EUC_KR"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {}

    attribute_map = {}

    def __init__(self):  # noqa: E501
        """ECIEncodings - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr in self.swagger_types:
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
        if issubclass(ECIEncodings, dict):
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
        if not isinstance(other, ECIEncodings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
