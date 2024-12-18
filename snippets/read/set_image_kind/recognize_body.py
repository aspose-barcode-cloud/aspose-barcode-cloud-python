import os
import base64
from aspose_barcode_cloud import (
    RecognizeApi,
    ApiClient,
    Configuration,
    DecodeBarcodeType,
    RecognizeBase64Request,
    RecognitionImageKind,
)

def make_configuration():
    jwt_token = os.getenv("TEST_CONFIGURATION_JWT_TOKEN")
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

    file_name = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        "..", "testdata", "aztec.png"
    ))

    with open(file_name, "rb") as file:
        image_bytes = file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Create the request with the appropriate Barcode types
    base64_request = RecognizeBase64Request(
        barcode_types=[DecodeBarcodeType.AZTEC, DecodeBarcodeType.QR],
        file_base64=image_base64,
        recognition_image_kind=RecognitionImageKind.SCANNEDDOCUMENT
    )

    # Make the API call
    result = recognize_api.recognize_base64(base64_request)

    # Print the outcome
    if result.barcodes:
        print(f"File '{file_name}' recognized, results: value: '{result.barcodes[0].barcode_value}', type: {result.barcodes[0].type}")
    else:
        print(f"File '{file_name}' recognized, but no barcodes found.")

if __name__ == "__main__":
    main()
