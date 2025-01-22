import os
from aspose_barcode_cloud import (
    RecognizeApi,
    ApiClient,
    Configuration,
    DecodeBarcodeType,
)


def make_configuration():
    jwt_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if jwt_token:
        config = Configuration(jwt_token=jwt_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():
    config = make_configuration()
    recognize_api = RecognizeApi(ApiClient(config))

    file_url = "https://products.aspose.app/barcode/scan/img/how-to/scan/step2.png"

    result = recognize_api.recognize(barcode_type=DecodeBarcodeType.QR, file_url=file_url)

    print(f"File '{file_url}' recognized, result: '{result.barcodes[0].barcode_value}'")


if __name__ == "__main__":
    main()
