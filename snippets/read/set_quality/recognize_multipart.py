import os
from aspose_barcode_cloud import (
    RecognizeApi,
    ApiClient,
    Configuration,
    DecodeBarcodeType,
    RecognitionImageKind,
    RecognitionMode,
)


def make_configuration():
    access_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if access_token:
        config = Configuration(access_token=access_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():
    config = make_configuration()
    recognize_api = RecognizeApi(ApiClient(config))

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "aztec.png"))

    with open(file_name, "rb") as file:
        file_content = file.read()
    result = recognize_api.recognize_multipart(
        DecodeBarcodeType.AZTEC, file_content, RecognitionMode.NORMAL, RecognitionImageKind.SCANNEDDOCUMENT
    )

    if result.barcodes:
        print(
            f"File '{file_name}' recognized, results: value: '{result.barcodes[0].barcode_value}', type: {result.barcodes[0].type}"
        )
    else:
        print(f"File '{file_name}' recognized, but no barcodes found.")


if __name__ == "__main__":
    main()
