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
VERSION = "21.3.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt"), "rt") as f:
    install_requires = [l.strip() for l in f]

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
    keywords=["Aspose", "Barcode", "Cloud"],
    install_requires=install_requires,
    packages=find_packages(exclude=["tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source With Tests": "https://github.com/aspose-barcode-cloud/aspose-barcode-cloud-python",
        "Website": "https://www.aspose.cloud",
        "Product Home": "https://products.aspose.cloud/barcode/cloud",
        "Documentation": "https://docs.aspose.cloud/barcode/",
        "Free Support Forum": "https://forum.aspose.cloud/c/barcode",
        "Paid Support Helpdesk": "https://helpdesk.aspose.cloud/",
        "Blog": "https://blog.aspose.cloud/category/barcode/",
    },
)
