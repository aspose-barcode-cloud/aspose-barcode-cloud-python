# Aspose.BarCode Cloud SDK for Python

[![License](https://img.shields.io/github/license/aspose-barcode-cloud/aspose-barcode-cloud-python)](LICENSE)
[![Python package](https://github.com/aspose-barcode-cloud/aspose-barcode-cloud-python/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/aspose-barcode-cloud/aspose-barcode-cloud-python/actions/workflows/python-package.yml)
[![PyPI](https://img.shields.io/pypi/v/aspose-barcode-cloud)](https://pypi.org/project/aspose-barcode-cloud/)

- API version: 3.0
- Package version: 24.13.0

## Demo applications

[Scan QR](https://products.aspose.app/barcode/scanqr) | [Generate Barcode](https://products.aspose.app/barcode/generate) | [Recognize Barcode](https://products.aspose.app/barcode/recognize)
:---: | :---: | :---:
[![ScanQR](https://products.aspose.app/barcode/scanqr/img/aspose_scanqr-app-48.png)](https://products.aspose.app/barcode/scanqr) | [![Generate](https://products.aspose.app/barcode/generate/img/aspose_generate-app-48.png)](https://products.aspose.app/barcode/generate) | [![Recognize](https://products.aspose.app/barcode/recognize/img/aspose_recognize-app-48.png)](https://products.aspose.app/barcode/recognize)
[**Generate Wi-Fi QR**](https://products.aspose.app/barcode/wifi-qr) | [**Embed Barcode**](https://products.aspose.app/barcode/embed) | [**Scan Barcode**](https://products.aspose.app/barcode/scan)
[![Wi-FiQR](https://products.aspose.app/barcode/embed/img/aspose_wifi-qr-app-48.png)](https://products.aspose.app/barcode/wifi-qr) | [![Embed](https://products.aspose.app/barcode/embed/img/aspose_embed-app-48.png)](https://products.aspose.app/barcode/embed) | [![Scan](https://products.aspose.app/barcode/embed/img/aspose_scan-app-48.png)](https://products.aspose.app/barcode/scan)

[Aspose.BarCode for Cloud](https://products.aspose.cloud/barcode/) is a REST API for Linear, 2D and postal barcode generation and recognition in the cloud. API recognizes and generates barcode images in a variety of formats. Barcode REST API allows to specify barcode image attributes like image width, height, border style and output image format in order to customize the generation process. Developers can also specify the barcode type and text attributes such as text location and font styles in order to suit the application requirements.

This repository contains Aspose.BarCode Cloud SDK for Python source code. This SDK allows you to work with Aspose.BarCode for Cloud REST APIs in your Python 3 applications quickly and easily.

Supported Python versions:

- Python 3.8+

To use these SDKs, you will need Client Id and Client Secret which can be looked up at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/applications) (free registration in Aspose Cloud is required for this).

## How to use the SDK

The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [from PyPi](https://pypi.org/project/aspose-barcode-cloud/) (recommended).

## Prerequisites

To use Aspose.BarCode Cloud SDK for Python you need to register an account with [Aspose Cloud](https://www.aspose.cloud) and lookup/create Client Secret and Client Id at [Cloud Dashboard](https://dashboard.aspose.cloud/applications). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/).

## Installation

### Install aspose-barcode-cloud via pip

From the command line:

```sh
pip install aspose-barcode-cloud
```

Then import the package:

```python
import aspose_barcode_cloud
```

## Sample usage

The examples below show how you can generate and recognize Code128 barcode and save it into local file using aspose-barcode-cloud:

```python
import os
from pprint import pprint

from aspose_barcode_cloud import (
    BarcodeApi,
    ApiClient,
    Configuration,
    EncodeBarcodeType,
    CodeLocation,
    DecodeBarcodeType,
)

config = Configuration(
    client_id="Client Id from https://dashboard.aspose.cloud/applications",
    client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
    access_token=os.environ.get("TEST_CONFIGURATION_ACCESS_TOKEN"),  # Only for testing in CI, remove this line
)

api = BarcodeApi(ApiClient(config))

# Generate barcode
response = api.get_barcode_generate(EncodeBarcodeType.QR, "Example", text_location=CodeLocation.NONE)
with open("example.png", "wb") as f:
    f.write(response.data)
print("Barcode saved to file 'example.png'")

# Recognize barcode
response = api.scan_barcode("example.png", decode_types=[DecodeBarcodeType.QR])
pprint(response)

```

## Requirements

- urllib3 >= 1.21.1, <2.0

## Licensing

All Aspose.BarCode for Cloud SDKs, helper scripts and templates are licensed under [MIT License](LICENSE).

## Resources

- [**Website**](https://www.aspose.cloud)
- [**Product Home**](https://products.aspose.cloud/barcode/)
- [**Documentation**](https://docs.aspose.cloud/barcode/)
- [**Free Support Forum**](https://forum.aspose.cloud/c/barcode)
- [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)
- [**Blog**](https://blog.aspose.cloud/categories/aspose.barcode-cloud-product-family/)

## Documentation for API Endpoints

All URIs are relative to *<https://api.aspose.cloud/v3.0>*

Class | Method | HTTP request | Description
----- | ------ | ------------ | -----------
*BarcodeApi* | [**get_barcode_generate**](docs/BarcodeApi.md#get_barcode_generate) | **GET** /barcode/generate | Generate barcode.
*BarcodeApi* | [**get_barcode_recognize**](docs/BarcodeApi.md#get_barcode_recognize) | **GET** /barcode/{name}/recognize | Recognize barcode from a file on server.
*BarcodeApi* | [**post_barcode_recognize_from_url_or_content**](docs/BarcodeApi.md#post_barcode_recognize_from_url_or_content) | **POST** /barcode/recognize | Recognize barcode from an url or from request body. Request body can contain raw data bytes of the image with content-type \&quot;application/octet-stream\&quot;. An image can also be passed as a form field.
*BarcodeApi* | [**post_generate_multiple**](docs/BarcodeApi.md#post_generate_multiple) | **POST** /barcode/generateMultiple | Generate multiple barcodes and return in response stream
*BarcodeApi* | [**put_barcode_generate_file**](docs/BarcodeApi.md#put_barcode_generate_file) | **PUT** /barcode/{name}/generate | Generate barcode and save on server (from query params or from file with json or xml content)
*BarcodeApi* | [**put_barcode_recognize_from_body**](docs/BarcodeApi.md#put_barcode_recognize_from_body) | **PUT** /barcode/{name}/recognize | Recognition of a barcode from file on server with parameters in body.
*BarcodeApi* | [**put_generate_multiple**](docs/BarcodeApi.md#put_generate_multiple) | **PUT** /barcode/{name}/generateMultiple | Generate image with multiple barcodes and put new file on server
*BarcodeApi* | [**scan_barcode**](docs/BarcodeApi.md#scan_barcode) | **POST** /barcode/scan | Quickly scan a barcode from an image.
*FileApi* | [**copy_file**](docs/FileApi.md#copy_file) | **PUT** /barcode/storage/file/copy/{srcPath} | Copy file
*FileApi* | [**delete_file**](docs/FileApi.md#delete_file) | **DELETE** /barcode/storage/file/{path} | Delete file
*FileApi* | [**download_file**](docs/FileApi.md#download_file) | **GET** /barcode/storage/file/{path} | Download file
*FileApi* | [**move_file**](docs/FileApi.md#move_file) | **PUT** /barcode/storage/file/move/{srcPath} | Move file
*FileApi* | [**upload_file**](docs/FileApi.md#upload_file) | **PUT** /barcode/storage/file/{path} | Upload file
*FolderApi* | [**copy_folder**](docs/FolderApi.md#copy_folder) | **PUT** /barcode/storage/folder/copy/{srcPath} | Copy folder
*FolderApi* | [**create_folder**](docs/FolderApi.md#create_folder) | **PUT** /barcode/storage/folder/{path} | Create the folder
*FolderApi* | [**delete_folder**](docs/FolderApi.md#delete_folder) | **DELETE** /barcode/storage/folder/{path} | Delete folder
*FolderApi* | [**get_files_list**](docs/FolderApi.md#get_files_list) | **GET** /barcode/storage/folder/{path} | Get all files and folders within a folder
*FolderApi* | [**move_folder**](docs/FolderApi.md#move_folder) | **PUT** /barcode/storage/folder/move/{srcPath} | Move folder
*StorageApi* | [**get_disc_usage**](docs/StorageApi.md#get_disc_usage) | **GET** /barcode/storage/disc | Get disc usage
*StorageApi* | [**get_file_versions**](docs/StorageApi.md#get_file_versions) | **GET** /barcode/storage/version/{path} | Get file versions
*StorageApi* | [**object_exists**](docs/StorageApi.md#object_exists) | **GET** /barcode/storage/exist/{path} | Check if file or folder exists
*StorageApi* | [**storage_exists**](docs/StorageApi.md#storage_exists) | **GET** /barcode/storage/{storageName}/exist | Check if storage exists

## Documentation For Models

- [ApiError](docs/ApiError.md)
- [ApiErrorResponse](docs/ApiErrorResponse.md)
- [AustralianPostParams](docs/AustralianPostParams.md)
- [AutoSizeMode](docs/AutoSizeMode.md)
- [AvailableGraphicsUnit](docs/AvailableGraphicsUnit.md)
- [AztecEncodeMode](docs/AztecEncodeMode.md)
- [AztecParams](docs/AztecParams.md)
- [AztecSymbolMode](docs/AztecSymbolMode.md)
- [BarcodeResponse](docs/BarcodeResponse.md)
- [BarcodeResponseList](docs/BarcodeResponseList.md)
- [BorderDashStyle](docs/BorderDashStyle.md)
- [CaptionParams](docs/CaptionParams.md)
- [ChecksumValidation](docs/ChecksumValidation.md)
- [CodabarChecksumMode](docs/CodabarChecksumMode.md)
- [CodabarParams](docs/CodabarParams.md)
- [CodabarSymbol](docs/CodabarSymbol.md)
- [CodablockParams](docs/CodablockParams.md)
- [Code128Emulation](docs/Code128Emulation.md)
- [Code128EncodeMode](docs/Code128EncodeMode.md)
- [Code128Params](docs/Code128Params.md)
- [Code16KParams](docs/Code16KParams.md)
- [CodeLocation](docs/CodeLocation.md)
- [CouponParams](docs/CouponParams.md)
- [CustomerInformationInterpretingType](docs/CustomerInformationInterpretingType.md)
- [DataBarParams](docs/DataBarParams.md)
- [DataMatrixEccType](docs/DataMatrixEccType.md)
- [DataMatrixEncodeMode](docs/DataMatrixEncodeMode.md)
- [DataMatrixParams](docs/DataMatrixParams.md)
- [DataMatrixVersion](docs/DataMatrixVersion.md)
- [DecodeBarcodeType](docs/DecodeBarcodeType.md)
- [DiscUsage](docs/DiscUsage.md)
- [DotCodeEncodeMode](docs/DotCodeEncodeMode.md)
- [DotCodeParams](docs/DotCodeParams.md)
- [ECIEncodings](docs/ECIEncodings.md)
- [EnableChecksum](docs/EnableChecksum.md)
- [EncodeBarcodeType](docs/EncodeBarcodeType.md)
- [Error](docs/Error.md)
- [ErrorDetails](docs/ErrorDetails.md)
- [FileVersions](docs/FileVersions.md)
- [FilesList](docs/FilesList.md)
- [FilesUploadResult](docs/FilesUploadResult.md)
- [FontMode](docs/FontMode.md)
- [FontParams](docs/FontParams.md)
- [FontStyle](docs/FontStyle.md)
- [GeneratorParams](docs/GeneratorParams.md)
- [GeneratorParamsList](docs/GeneratorParamsList.md)
- [HanXinEncodeMode](docs/HanXinEncodeMode.md)
- [HanXinErrorLevel](docs/HanXinErrorLevel.md)
- [HanXinParams](docs/HanXinParams.md)
- [HanXinVersion](docs/HanXinVersion.md)
- [ITF14BorderType](docs/ITF14BorderType.md)
- [ITFParams](docs/ITFParams.md)
- [MacroCharacter](docs/MacroCharacter.md)
- [MaxiCodeEncodeMode](docs/MaxiCodeEncodeMode.md)
- [MaxiCodeMode](docs/MaxiCodeMode.md)
- [MaxiCodeParams](docs/MaxiCodeParams.md)
- [ObjectExist](docs/ObjectExist.md)
- [Padding](docs/Padding.md)
- [PatchCodeParams](docs/PatchCodeParams.md)
- [PatchFormat](docs/PatchFormat.md)
- [Pdf417CompactionMode](docs/Pdf417CompactionMode.md)
- [Pdf417ErrorLevel](docs/Pdf417ErrorLevel.md)
- [Pdf417MacroTerminator](docs/Pdf417MacroTerminator.md)
- [Pdf417Params](docs/Pdf417Params.md)
- [PostalParams](docs/PostalParams.md)
- [PresetType](docs/PresetType.md)
- [QREncodeMode](docs/QREncodeMode.md)
- [QREncodeType](docs/QREncodeType.md)
- [QRErrorLevel](docs/QRErrorLevel.md)
- [QRVersion](docs/QRVersion.md)
- [QrParams](docs/QrParams.md)
- [ReaderParams](docs/ReaderParams.md)
- [RegionPoint](docs/RegionPoint.md)
- [ResultImageInfo](docs/ResultImageInfo.md)
- [StorageExist](docs/StorageExist.md)
- [StorageFile](docs/StorageFile.md)
- [StructuredAppend](docs/StructuredAppend.md)
- [TextAlignment](docs/TextAlignment.md)
- [FileVersion](docs/FileVersion.md)


