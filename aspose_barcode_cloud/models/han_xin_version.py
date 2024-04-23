# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401

import six


class HanXinVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AUTO = "Auto"
    VERSION01 = "Version01"
    VERSION02 = "Version02"
    VERSION03 = "Version03"
    VERSION04 = "Version04"
    VERSION05 = "Version05"
    VERSION06 = "Version06"
    VERSION07 = "Version07"
    VERSION08 = "Version08"
    VERSION09 = "Version09"
    VERSION10 = "Version10"
    VERSION11 = "Version11"
    VERSION12 = "Version12"
    VERSION13 = "Version13"
    VERSION14 = "Version14"
    VERSION15 = "Version15"
    VERSION16 = "Version16"
    VERSION17 = "Version17"
    VERSION18 = "Version18"
    VERSION19 = "Version19"
    VERSION20 = "Version20"
    VERSION21 = "Version21"
    VERSION22 = "Version22"
    VERSION23 = "Version23"
    VERSION24 = "Version24"
    VERSION25 = "Version25"
    VERSION26 = "Version26"
    VERSION27 = "Version27"
    VERSION28 = "Version28"
    VERSION29 = "Version29"
    VERSION30 = "Version30"
    VERSION31 = "Version31"
    VERSION32 = "Version32"
    VERSION33 = "Version33"
    VERSION34 = "Version34"
    VERSION35 = "Version35"
    VERSION36 = "Version36"
    VERSION37 = "Version37"
    VERSION38 = "Version38"
    VERSION39 = "Version39"
    VERSION40 = "Version40"
    VERSION41 = "Version41"
    VERSION42 = "Version42"
    VERSION43 = "Version43"
    VERSION44 = "Version44"
    VERSION45 = "Version45"
    VERSION46 = "Version46"
    VERSION47 = "Version47"
    VERSION48 = "Version48"
    VERSION49 = "Version49"
    VERSION50 = "Version50"
    VERSION51 = "Version51"
    VERSION52 = "Version52"
    VERSION53 = "Version53"
    VERSION54 = "Version54"
    VERSION55 = "Version55"
    VERSION56 = "Version56"
    VERSION57 = "Version57"
    VERSION58 = "Version58"
    VERSION59 = "Version59"
    VERSION60 = "Version60"
    VERSION61 = "Version61"
    VERSION62 = "Version62"
    VERSION63 = "Version63"
    VERSION64 = "Version64"
    VERSION65 = "Version65"
    VERSION66 = "Version66"
    VERSION67 = "Version67"
    VERSION68 = "Version68"
    VERSION69 = "Version69"
    VERSION70 = "Version70"
    VERSION71 = "Version71"
    VERSION72 = "Version72"
    VERSION73 = "Version73"
    VERSION74 = "Version74"
    VERSION75 = "Version75"
    VERSION76 = "Version76"
    VERSION77 = "Version77"
    VERSION78 = "Version78"
    VERSION79 = "Version79"
    VERSION80 = "Version80"
    VERSION81 = "Version81"
    VERSION82 = "Version82"
    VERSION83 = "Version83"
    VERSION84 = "Version84"

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
        """HanXinVersion - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(HanXinVersion, dict):
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
        if not isinstance(other, HanXinVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
