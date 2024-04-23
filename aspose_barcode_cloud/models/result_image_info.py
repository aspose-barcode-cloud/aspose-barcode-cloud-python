# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401

import six


class ResultImageInfo(object):
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
    swagger_types = {"file_size": "int", "image_width": "int", "image_height": "int"}

    attribute_map = {"file_size": "FileSize", "image_width": "ImageWidth", "image_height": "ImageHeight"}

    def __init__(self, file_size=None, image_width=None, image_height=None):  # noqa: E501
        """ResultImageInfo - a model defined in Swagger"""  # noqa: E501

        self._file_size = None
        self._image_width = None
        self._image_height = None
        self.discriminator = None

        self.file_size = file_size
        if image_width is not None:
            self.image_width = image_width
        if image_height is not None:
            self.image_height = image_height

    @property
    def file_size(self):
        """Gets the file_size of this ResultImageInfo.  # noqa: E501

        Result file size.  # noqa: E501

        :return: The file_size of this ResultImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ResultImageInfo.

        Result file size.  # noqa: E501

        :param file_size: The file_size of this ResultImageInfo.  # noqa: E501
        :type: int
        """
        if file_size is None:
            raise ValueError("Invalid value for `file_size`, must not be `None`")  # noqa: E501

        self._file_size = file_size

    @property
    def image_width(self):
        """Gets the image_width of this ResultImageInfo.  # noqa: E501

        Result image width.  # noqa: E501

        :return: The image_width of this ResultImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this ResultImageInfo.

        Result image width.  # noqa: E501

        :param image_width: The image_width of this ResultImageInfo.  # noqa: E501
        :type: int
        """

        self._image_width = image_width

    @property
    def image_height(self):
        """Gets the image_height of this ResultImageInfo.  # noqa: E501

        Result image height.  # noqa: E501

        :return: The image_height of this ResultImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """Sets the image_height of this ResultImageInfo.

        Result image height.  # noqa: E501

        :param image_height: The image_height of this ResultImageInfo.  # noqa: E501
        :type: int
        """

        self._image_height = image_height

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
        if issubclass(ResultImageInfo, dict):
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
        if not isinstance(other, ResultImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
