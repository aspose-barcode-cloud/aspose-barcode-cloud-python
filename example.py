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
