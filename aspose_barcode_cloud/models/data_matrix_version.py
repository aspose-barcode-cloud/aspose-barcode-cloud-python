# coding: utf-8

import pprint
import re  # noqa: F401
import warnings  # noqa: F401

import six


class DataMatrixVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    AUTO = "Auto"
    ROWSCOLUMNS = "RowsColumns"
    ECC000_9X9 = "ECC000_9x9"
    ECC000_050_11X11 = "ECC000_050_11x11"
    ECC000_100_13X13 = "ECC000_100_13x13"
    ECC000_100_15X15 = "ECC000_100_15x15"
    ECC000_140_17X17 = "ECC000_140_17x17"
    ECC000_140_19X19 = "ECC000_140_19x19"
    ECC000_140_21X21 = "ECC000_140_21x21"
    ECC000_140_23X23 = "ECC000_140_23x23"
    ECC000_140_25X25 = "ECC000_140_25x25"
    ECC000_140_27X27 = "ECC000_140_27x27"
    ECC000_140_29X29 = "ECC000_140_29x29"
    ECC000_140_31X31 = "ECC000_140_31x31"
    ECC000_140_33X33 = "ECC000_140_33x33"
    ECC000_140_35X35 = "ECC000_140_35x35"
    ECC000_140_37X37 = "ECC000_140_37x37"
    ECC000_140_39X39 = "ECC000_140_39x39"
    ECC000_140_41X41 = "ECC000_140_41x41"
    ECC000_140_43X43 = "ECC000_140_43x43"
    ECC000_140_45X45 = "ECC000_140_45x45"
    ECC000_140_47X47 = "ECC000_140_47x47"
    ECC000_140_49X49 = "ECC000_140_49x49"
    ECC200_10X10 = "ECC200_10x10"
    ECC200_12X12 = "ECC200_12x12"
    ECC200_14X14 = "ECC200_14x14"
    ECC200_16X16 = "ECC200_16x16"
    ECC200_18X18 = "ECC200_18x18"
    ECC200_20X20 = "ECC200_20x20"
    ECC200_22X22 = "ECC200_22x22"
    ECC200_24X24 = "ECC200_24x24"
    ECC200_26X26 = "ECC200_26x26"
    ECC200_32X32 = "ECC200_32x32"
    ECC200_36X36 = "ECC200_36x36"
    ECC200_40X40 = "ECC200_40x40"
    ECC200_44X44 = "ECC200_44x44"
    ECC200_48X48 = "ECC200_48x48"
    ECC200_52X52 = "ECC200_52x52"
    ECC200_64X64 = "ECC200_64x64"
    ECC200_72X72 = "ECC200_72x72"
    ECC200_80X80 = "ECC200_80x80"
    ECC200_88X88 = "ECC200_88x88"
    ECC200_96X96 = "ECC200_96x96"
    ECC200_104X104 = "ECC200_104x104"
    ECC200_120X120 = "ECC200_120x120"
    ECC200_132X132 = "ECC200_132x132"
    ECC200_144X144 = "ECC200_144x144"
    ECC200_8X18 = "ECC200_8x18"
    ECC200_8X32 = "ECC200_8x32"
    ECC200_12X26 = "ECC200_12x26"
    ECC200_12X36 = "ECC200_12x36"
    ECC200_16X36 = "ECC200_16x36"
    ECC200_16X48 = "ECC200_16x48"
    DMRE_8X48 = "DMRE_8x48"
    DMRE_8X64 = "DMRE_8x64"
    DMRE_8X80 = "DMRE_8x80"
    DMRE_8X96 = "DMRE_8x96"
    DMRE_8X120 = "DMRE_8x120"
    DMRE_8X144 = "DMRE_8x144"
    DMRE_12X64 = "DMRE_12x64"
    DMRE_12X88 = "DMRE_12x88"
    DMRE_16X64 = "DMRE_16x64"
    DMRE_20X36 = "DMRE_20x36"
    DMRE_20X44 = "DMRE_20x44"
    DMRE_20X64 = "DMRE_20x64"
    DMRE_22X48 = "DMRE_22x48"
    DMRE_24X48 = "DMRE_24x48"
    DMRE_24X64 = "DMRE_24x64"
    DMRE_26X40 = "DMRE_26x40"
    DMRE_26X48 = "DMRE_26x48"
    DMRE_26X64 = "DMRE_26x64"

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
        """DataMatrixVersion - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(DataMatrixVersion, dict):
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
        if not isinstance(other, DataMatrixVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
