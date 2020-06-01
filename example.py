from __future__ import division, print_function

import os
from pprint import pprint

from aspose_barcode_cloud import BarcodeApi, ApiClient, Configuration, EncodeBarcodeType, PresetType

config = Configuration(
    app_sid="App SID from https://dashboard.aspose.cloud/#/apps",
    app_key="App Key from https://dashboard.aspose.cloud/#/apps",
)

api = BarcodeApi(ApiClient(config))

# Generate barcode
response = api.get_barcode_generate(EncodeBarcodeType.QR, "Example")
with open('example.png', 'wb') as f:
    f.write(response.data)
print("Barcode saved to file 'example.png'")

# Recognize barcode
response = api.post_barcode_recognize_from_url_or_content(image='example.png', preset=PresetType.HIGHPERFORMANCE)
pprint(response)
