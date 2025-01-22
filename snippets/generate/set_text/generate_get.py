import os
from aspose_barcode_cloud import (
    ApiClient,
    Configuration,
    EncodeBarcodeType,
    EncodeData,
    EncodeDataType,
    GenerateParams,
    BarcodeImageParams,
    BarcodeImageFormat,
)
from aspose_barcode_cloud.api.generate_api import GenerateApi


def make_configuration():
    env_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if env_token:
        config = Configuration(jwt_token=env_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():
    """Main function to generate a QR code."""
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    generate_api = GenerateApi(api_client=api_client)

    generate_params = GenerateParams(
        EncodeBarcodeType.QR, EncodeData(EncodeDataType.STRINGDATA, "Aspose.BarCode.Cloud")
    )

    response = generate_api.generate_body(generate_params)

    with open(file_name, "wb") as file_stream:
        file_stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
