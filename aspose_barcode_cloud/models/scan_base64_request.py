# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401


class ScanBase64Request(object):
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
    swagger_types = {"file_base64": "str"}

    attribute_map = {"file_base64": "fileBase64"}

    def __init__(self, file_base64=None):  # noqa: E501
        """ScanBase64Request - a model defined in Swagger"""  # noqa: E501

        self._file_base64 = None
        self.discriminator = None

        self.file_base64 = file_base64

    @property
    def file_base64(self):
        """Gets the file_base64 of this ScanBase64Request.  # noqa: E501

        Barcode image bytes encoded as base-64.  # noqa: E501

        :return: The file_base64 of this ScanBase64Request.  # noqa: E501
        :rtype: str
        """
        return self._file_base64

    @file_base64.setter
    def file_base64(self, file_base64):
        """Sets the file_base64 of this ScanBase64Request.

        Barcode image bytes encoded as base-64.  # noqa: E501

        :param file_base64: The file_base64 of this ScanBase64Request.  # noqa: E501
        :type: str
        """
        if file_base64 is None:
            raise ValueError("Invalid value for `file_base64`, must not be `None`")  # noqa: E501
        if file_base64 is not None and len(file_base64) < 1:
            raise ValueError(
                "Invalid value for `file_base64`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._file_base64 = file_base64

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
        if issubclass(ScanBase64Request, dict):
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
        if not isinstance(other, ScanBase64Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other