# coding: utf-8

"""

    Copyright (c) 2021 Aspose.BarCode for Cloud

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

import os

from setuptools import setup, find_packages

NAME = "aspose-barcode-cloud"
VERSION = "21.9.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "rt") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.Barcode Cloud API Reference",
    author="Aspose Barcode Cloud",
    url="https://github.com/aspose-barcode-cloud/aspose-barcode-cloud-python",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords=[
        "JPEG",
        "TIFF",
        "PNG",
        "BMP",
        "GIF",
        "EXIF",
        "EMF",
        "SVG",
        "Aspose.BarCode",
        "Aspose.BarCode-Cloud",
        "Aspose.Total-Cloud",
        "Cloud",
        "REST",
        "API",
        "Barcode",
        "Generate-Barcode",
        "Barcode-Generation",
        "Barcode-Formatting",
        "Format-Barcode",
        "Barcode-Recognition",
        "Recognize-Barcode",
        "Symbology",
        "Codetext",
        "CodablockF",
        "Checksum",
        "Optimize-Barcode",
        "Barcode-Optimization",
        "cURL",
        ".NET",
        "C#",
        "dotnet",
        "CSharp",
        "Java",
        "PHP",
        "Python",
        "Node.js",
        "Golang",
        "1D-Barcode",
        "2D-Barcode",
        "Postal-Barcode",
        "Barcode-Scan",
        "Scan-Barcode",
        "barcode",
        "generation",
        "recognition",
        "Alpha-Numeric",
        "AI-8102-Coupon",
        "AustralianPosteParcel",
        "AustraliaPost",
        "Aztec",
        "Codabar",
        "Code11",
        "Code128",
        "Code16K",
        "Code32",
        "Code39Extended",
        "Code39Standard",
        "Code93Extended",
        "Code93Standard",
        "DatabarExpanded",
        "DatabarExpandedStacked",
        "DatabarLimited",
        "DatabarOmniDirectional",
        "DatabarStacked",
        "DatabarStackedOmniDirectional",
        "DatabarTruncated",
        "DataLogic2of5",
        "DataMatrix",
        "DeutschePostIdentcode",
        "DeutschePostLeitcode",
        "DotCode",
        "DutchKIX",
        "EAN13",
        "EAN14",
        "EAN8",
        "GS1CodablockF",
        "GS1Code128",
        "GS1DataMatrix",
        "GS1QR",
        "IATA2of5",
        "Interleaved2of5",
        "ISBN",
        "ISMN",
        "ISSN",
        "ItalianPost25",
        "ITF14",
        "ITF6",
        "MacroPdf417",
        "Matrix2of5",
        "MaxiCode",
        "MicroPdf417",
        "MICR",
        "MSI",
        "OneCode",
        "OPC",
        "PatchCode",
        "Pdf417",
        "Pharmacode",
        "Planet",
        "Postnet",
        "PZN",
        "QR",
        "RM4SCC",
        "SCC14",
        "SingaporePost",
        "SSCC18",
        "Standard2of5",
        "SwissPostParcel",
        "UPCA",
        "UpcaGs1Code128Coupon",
        "UpcaGs1DatabarCoupon",
        "UPCE",
        "VIN"
    ],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source With Tests": "https://github.com/aspose-barcode-cloud/aspose-barcode-cloud-python",
        "Website": "https://www.aspose.cloud",
        "Product Home": "https://products.aspose.cloud/barcode/",
        "Documentation": "https://docs.aspose.cloud/barcode/",
        "Free Support Forum": "https://forum.aspose.cloud/c/barcode",
        "Paid Support Helpdesk": "https://helpdesk.aspose.cloud/",
        "Blog": "https://blog.aspose.cloud/category/barcode/",
    },
)
