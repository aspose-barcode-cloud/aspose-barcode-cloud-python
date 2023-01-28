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

import six


class EncodeBarcodeType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CODABAR = "Codabar"
    CODE11 = "Code11"
    CODE39STANDARD = "Code39Standard"
    CODE39EXTENDED = "Code39Extended"
    CODE93STANDARD = "Code93Standard"
    CODE93EXTENDED = "Code93Extended"
    CODE128 = "Code128"
    GS1CODE128 = "GS1Code128"
    EAN8 = "EAN8"
    EAN13 = "EAN13"
    EAN14 = "EAN14"
    SCC14 = "SCC14"
    SSCC18 = "SSCC18"
    UPCA = "UPCA"
    UPCE = "UPCE"
    ISBN = "ISBN"
    ISSN = "ISSN"
    ISMN = "ISMN"
    STANDARD2OF5 = "Standard2of5"
    INTERLEAVED2OF5 = "Interleaved2of5"
    MATRIX2OF5 = "Matrix2of5"
    ITALIANPOST25 = "ItalianPost25"
    IATA2OF5 = "IATA2of5"
    ITF14 = "ITF14"
    ITF6 = "ITF6"
    MSI = "MSI"
    VIN = "VIN"
    DEUTSCHEPOSTIDENTCODE = "DeutschePostIdentcode"
    DEUTSCHEPOSTLEITCODE = "DeutschePostLeitcode"
    OPC = "OPC"
    PZN = "PZN"
    CODE16K = "Code16K"
    PHARMACODE = "Pharmacode"
    DATAMATRIX = "DataMatrix"
    QR = "QR"
    AZTEC = "Aztec"
    PDF417 = "Pdf417"
    MACROPDF417 = "MacroPdf417"
    AUSTRALIAPOST = "AustraliaPost"
    POSTNET = "Postnet"
    PLANET = "Planet"
    ONECODE = "OneCode"
    RM4SCC = "RM4SCC"
    DATABAROMNIDIRECTIONAL = "DatabarOmniDirectional"
    DATABARTRUNCATED = "DatabarTruncated"
    DATABARLIMITED = "DatabarLimited"
    DATABAREXPANDED = "DatabarExpanded"
    SINGAPOREPOST = "SingaporePost"
    GS1DATAMATRIX = "GS1DataMatrix"
    AUSTRALIANPOSTEPARCEL = "AustralianPosteParcel"
    SWISSPOSTPARCEL = "SwissPostParcel"
    PATCHCODE = "PatchCode"
    DATABAREXPANDEDSTACKED = "DatabarExpandedStacked"
    DATABARSTACKED = "DatabarStacked"
    DATABARSTACKEDOMNIDIRECTIONAL = "DatabarStackedOmniDirectional"
    MICROPDF417 = "MicroPdf417"
    GS1QR = "GS1QR"
    MAXICODE = "MaxiCode"
    CODE32 = "Code32"
    DATALOGIC2OF5 = "DataLogic2of5"
    DOTCODE = "DotCode"
    DUTCHKIX = "DutchKIX"
    UPCAGS1CODE128COUPON = "UpcaGs1Code128Coupon"
    UPCAGS1DATABARCOUPON = "UpcaGs1DatabarCoupon"
    CODABLOCKF = "CodablockF"
    GS1CODABLOCKF = "GS1CodablockF"
    MAILMARK = "Mailmark"
    GS1DOTCODE = "GS1DotCode"

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
        """EncodeBarcodeType - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(EncodeBarcodeType, dict):
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
        if not isinstance(other, EncodeBarcodeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
