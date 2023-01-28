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

import os

from setuptools import setup, find_packages

NAME = "aspose-barcode-cloud"
VERSION = "23.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["certifi>=2017.4.17", "python-dateutil>=2.1", "six>=1.10", "urllib3>=1.23"]

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
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=[
        "Barcode-Scan",
        "QR",
        "DataMatrix",
        "Barcode",
        "AustraliaPost",
        "VIN",
        "MSI",
        "Aztec",
        "ISBN",
        "OPC",
        "Postnet",
        "2D-Barcode",
        "EAN13",
        "ISSN",
        "PZN",
        "SingaporePost",
        "Symbology",
        "UPCA",
        "UPCE",
        "1D-Barcode",
        "Code11",
        "Code128",
        "Code32",
        "Codetext",
        "DotCode",
        "EAN14",
        "EAN8",
        "GS1DataMatrix",
        "Interleaved2of5",
        "ISMN",
        "MaxiCode",
        "OneCode",
        "Pdf417",
        "Pharmacode",
        "Postal-Barcode",
        "RM4SCC",
        "SCC14",
        "SSCC18",
        "Code39Standard",
        "GS1QR",
        "MacroPdf417",
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
        "Generate-Barcode",
        "Barcode-Generation",
        "Barcode-Formatting",
        "Format-Barcode",
        "Barcode-Recognition",
        "Recognize-Barcode",
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
        "Scan-Barcode",
        "barcode",
        "generation",
        "recognition",
        "Alpha-Numeric",
        "AI-8102-Coupon",
        "AustralianPosteParcel",
        "Codabar",
        "Code16K",
        "Code39Extended",
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
        "DeutschePostIdentcode",
        "DeutschePostLeitcode",
        "DutchKIX",
        "GS1CodablockF",
        "GS1Code128",
        "IATA2of5",
        "ItalianPost25",
        "ITF14",
        "ITF6",
        "Matrix2of5",
        "MicroPdf417",
        "MICR",
        "PatchCode",
        "Planet",
        "Standard2of5",
        "SwissPostParcel",
        "UpcaGs1Code128Coupon",
        "UpcaGs1DatabarCoupon",
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
        "Blog": "https://blog.aspose.cloud/categories/aspose.barcode-cloud-product-family/",
    },
)
