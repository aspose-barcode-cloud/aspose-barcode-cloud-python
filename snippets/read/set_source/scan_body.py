import os
import base64
from aspose_barcode_cloud import ScanApi, ApiClient, Configuration, ScanBase64Request


def make_configuration():
    env_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if not env_token:
        return Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    else:
        return Configuration(access_token=env_token)


def main():
    scan_api = ScanApi(ApiClient(make_configuration()))

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    with open(file_name, "rb") as file:
        image_bytes = file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    request = ScanBase64Request(file_base64=image_base64)
    result = scan_api.scan_base64(request)

    print(f"File '{file_name}' recognized, result: '{result.barcodes[0].barcode_value}'")
