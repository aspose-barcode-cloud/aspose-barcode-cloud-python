# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401


class CodablockParams(object):
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
    swagger_types = {"aspect_ratio": "float", "columns": "int", "rows": "int"}

    attribute_map = {"aspect_ratio": "AspectRatio", "columns": "Columns", "rows": "Rows"}

    def __init__(self, aspect_ratio=None, columns=None, rows=None):  # noqa: E501
        """CodablockParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._columns = None
        self._rows = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if columns is not None:
            self.columns = columns
        if rows is not None:
            self.rows = rows

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this CodablockParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :return: The aspect_ratio of this CodablockParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this CodablockParams.

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this CodablockParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def columns(self):
        """Gets the columns of this CodablockParams.  # noqa: E501

        Columns count.  # noqa: E501

        :return: The columns of this CodablockParams.  # noqa: E501
        :rtype: int
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CodablockParams.

        Columns count.  # noqa: E501

        :param columns: The columns of this CodablockParams.  # noqa: E501
        :type: int
        """

        self._columns = columns

    @property
    def rows(self):
        """Gets the rows of this CodablockParams.  # noqa: E501

        Rows count.  # noqa: E501

        :return: The rows of this CodablockParams.  # noqa: E501
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this CodablockParams.

        Rows count.  # noqa: E501

        :param rows: The rows of this CodablockParams.  # noqa: E501
        :type: int
        """

        self._rows = rows

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
        if issubclass(CodablockParams, dict):
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
        if not isinstance(other, CodablockParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
