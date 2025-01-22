import os
from aspose_barcode_cloud import (
    RecognizeApi,
    ApiClient,
    Configuration,
    DecodeBarcodeType,
)

# Function to create configuration
def make_configuration():
    env_token = os.getenv("TEST_CONFIGURATION_JWT_TOKEN")
    if env_token:
        config = Configuration(jwt_token=env_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():

    recognize_api = RecognizeApi(ApiClient(make_configuration()))

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    with open(file_path, "rb") as file_stream:
        result = recognize_api.recognize_multipart(barcode_type=DecodeBarcodeType.QR, file=file_stream)

    if result.barcodes:
        print(f"File '{file_path}' recognized, result: '{result.barcodes[0].barcode_value}'")
    else:
        print(f"No barcodes found in '{file_path}'.")


if __name__ == "__main__":
    main()
