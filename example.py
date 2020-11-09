from __future__ import division, print_function

import os
from pprint import pprint

from aspose_barcode_cloud import BarcodeApi, ApiClient, Configuration, EncodeBarcodeType, PresetType

config = Configuration(
    client_id="Client Id from https://dashboard.aspose.cloud/#/apps",
    client_secret="Client Secret from https://dashboard.aspose.cloud/#/apps",
    access_token=os.environ.get("TEST_ACCESS_TOKEN")  # Only for testing in CI, remove this line
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
