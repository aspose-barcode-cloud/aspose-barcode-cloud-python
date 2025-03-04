# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401


class ApiError(object):
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
        "code": "str",
        "message": "str",
        "description": "str",
        "date_time": "datetime",
        "inner_error": "ApiError",
    }

    attribute_map = {
        "code": "code",
        "message": "message",
        "description": "description",
        "date_time": "dateTime",
        "inner_error": "innerError",
    }

    def __init__(self, code=None, message=None, description=None, date_time=None, inner_error=None):  # noqa: E501
        """ApiError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._message = None
        self._description = None
        self._date_time = None
        self._inner_error = None
        self.discriminator = None

        self.code = code
        self.message = message
        if description is not None:
            self.description = description
        if date_time is not None:
            self.date_time = date_time
        if inner_error is not None:
            self.inner_error = inner_error

    @property
    def code(self):
        """Gets the code of this ApiError.  # noqa: E501

        Gets or sets api error code.  # noqa: E501

        :return: The code of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApiError.

        Gets or sets api error code.  # noqa: E501

        :param code: The code of this ApiError.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this ApiError.  # noqa: E501

        Gets or sets error message.  # noqa: E501

        :return: The message of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiError.

        Gets or sets error message.  # noqa: E501

        :param message: The message of this ApiError.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def description(self):
        """Gets the description of this ApiError.  # noqa: E501

        Gets or sets error description.  # noqa: E501

        :return: The description of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiError.

        Gets or sets error description.  # noqa: E501

        :param description: The description of this ApiError.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def date_time(self):
        """Gets the date_time of this ApiError.  # noqa: E501

        Gets or sets server datetime.  # noqa: E501

        :return: The date_time of this ApiError.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this ApiError.

        Gets or sets server datetime.  # noqa: E501

        :param date_time: The date_time of this ApiError.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def inner_error(self):
        """Gets the inner_error of this ApiError.  # noqa: E501


        :return: The inner_error of this ApiError.  # noqa: E501
        :rtype: ApiError
        """
        return self._inner_error

    @inner_error.setter
    def inner_error(self, inner_error):
        """Sets the inner_error of this ApiError.


        :param inner_error: The inner_error of this ApiError.  # noqa: E501
        :type: ApiError
        """

        self._inner_error = inner_error

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
        if issubclass(ApiError, dict):
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
        if not isinstance(other, ApiError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
