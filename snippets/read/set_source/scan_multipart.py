import os
from pathlib import Path

from aspose_barcode_cloud import ApiClient, Configuration, ScanApi


def make_configuration():
    env_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if env_token:
        return Configuration(jwt_token=env_token)
    else:
        return Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )


def main():
    scan_api = ScanApi(ApiClient(make_configuration()))

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    with open(file_name, "rb") as file_stream:
        result = scan_api.scan_multipart(file=file_stream)

    print(f"File '{file_name}' recognized, result: '{result.barcodes[0].barcode_value}'")


if __name__ == "__main__":
    main()
