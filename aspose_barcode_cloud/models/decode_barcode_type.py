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


class DecodeBarcodeType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ALL = "all"
    AUSTRALIAPOST = "AustraliaPost"
    AZTEC = "Aztec"
    ISBN = "ISBN"
    CODABAR = "Codabar"
    CODE11 = "Code11"
    CODE128 = "Code128"
    GS1CODE128 = "GS1Code128"
    CODE39EXTENDED = "Code39Extended"
    CODE39STANDARD = "Code39Standard"
    CODE93EXTENDED = "Code93Extended"
    CODE93STANDARD = "Code93Standard"
    DATAMATRIX = "DataMatrix"
    DEUTSCHEPOSTIDENTCODE = "DeutschePostIdentcode"
    DEUTSCHEPOSTLEITCODE = "DeutschePostLeitcode"
    EAN13 = "EAN13"
    EAN14 = "EAN14"
    EAN8 = "EAN8"
    IATA2OF5 = "IATA2of5"
    INTERLEAVED2OF5 = "Interleaved2of5"
    ISSN = "ISSN"
    ISMN = "ISMN"
    ITALIANPOST25 = "ItalianPost25"
    ITF14 = "ITF14"
    ITF6 = "ITF6"
    MACROPDF417 = "MacroPdf417"
    MATRIX2OF5 = "Matrix2of5"
    MSI = "MSI"
    ONECODE = "OneCode"
    OPC = "OPC"
    PATCHCODE = "PatchCode"
    PDF417 = "Pdf417"
    MICROPDF417 = "MicroPdf417"
    PLANET = "Planet"
    POSTNET = "Postnet"
    PZN = "PZN"
    QR = "QR"
    MICROQR = "MicroQR"
    RM4SCC = "RM4SCC"
    SCC14 = "SCC14"
    SSCC18 = "SSCC18"
    STANDARD2OF5 = "Standard2of5"
    SUPPLEMENT = "Supplement"
    UPCA = "UPCA"
    UPCE = "UPCE"
    VIN = "VIN"
    PHARMACODE = "Pharmacode"
    GS1DATAMATRIX = "GS1DataMatrix"
    DATABAROMNIDIRECTIONAL = "DatabarOmniDirectional"
    DATABARTRUNCATED = "DatabarTruncated"
    DATABARLIMITED = "DatabarLimited"
    DATABAREXPANDED = "DatabarExpanded"
    SWISSPOSTPARCEL = "SwissPostParcel"
    AUSTRALIANPOSTEPARCEL = "AustralianPosteParcel"
    CODE16K = "Code16K"
    DATABARSTACKEDOMNIDIRECTIONAL = "DatabarStackedOmniDirectional"
    DATABARSTACKED = "DatabarStacked"
    DATABAREXPANDEDSTACKED = "DatabarExpandedStacked"
    COMPACTPDF417 = "CompactPdf417"
    GS1QR = "GS1QR"
    MAXICODE = "MaxiCode"
    MICRE13B = "MicrE13B"
    CODE32 = "Code32"
    DATALOGIC2OF5 = "DataLogic2of5"
    DOTCODE = "DotCode"
    DUTCHKIX = "DutchKIX"
    CODABLOCKF = "CodablockF"
    MAILMARK = "Mailmark"
    GS1DOTCODE = "GS1DotCode"
    HIBCCODE39LIC = "HIBCCode39LIC"
    HIBCCODE128LIC = "HIBCCode128LIC"
    HIBCAZTECLIC = "HIBCAztecLIC"
    HIBCDATAMATRIXLIC = "HIBCDataMatrixLIC"
    HIBCQRLIC = "HIBCQRLIC"
    HIBCCODE39PAS = "HIBCCode39PAS"
    HIBCCODE128PAS = "HIBCCode128PAS"
    HIBCAZTECPAS = "HIBCAztecPAS"
    HIBCDATAMATRIXPAS = "HIBCDataMatrixPAS"
    HIBCQRPAS = "HIBCQRPAS"
    HANXIN = "HanXin"
    GS1HANXIN = "GS1HanXin"
    GS1AZTEC = "GS1Aztec"
    GS1COMPOSITEBAR = "GS1CompositeBar"

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
        """DecodeBarcodeType - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(DecodeBarcodeType, dict):
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
        if not isinstance(other, DecodeBarcodeType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
