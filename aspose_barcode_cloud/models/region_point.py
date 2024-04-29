# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401

import six


class RegionPoint(object):
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
    swagger_types = {"x": "int", "y": "int"}

    attribute_map = {"x": "X", "y": "Y"}

    def __init__(self, x=None, y=None):  # noqa: E501
        """RegionPoint - a model defined in Swagger"""  # noqa: E501

        self._x = None
        self._y = None
        self.discriminator = None

        self.x = x
        self.y = y

    @property
    def x(self):
        """Gets the x of this RegionPoint.  # noqa: E501

        X-coordinate  # noqa: E501

        :return: The x of this RegionPoint.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this RegionPoint.

        X-coordinate  # noqa: E501

        :param x: The x of this RegionPoint.  # noqa: E501
        :type: int
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this RegionPoint.  # noqa: E501

        Y-coordinate  # noqa: E501

        :return: The y of this RegionPoint.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this RegionPoint.

        Y-coordinate  # noqa: E501

        :param y: The y of this RegionPoint.  # noqa: E501
        :type: int
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

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
        if issubclass(RegionPoint, dict):
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
        if not isinstance(other, RegionPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
