import os
from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    GenerateParams,
    BarcodeImageParams,
    BarcodeImageFormat,
    EncodeData,
    EncodeDataType,
    Configuration,
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
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    generate_api = GenerateApi(api_client=api_client)

    generator_params = GenerateParams(
        EncodeBarcodeType.QR,
        EncodeData(EncodeDataType.STRINGDATA, "Aspose.BarCode.Cloud"),
        BarcodeImageParams(
            BarcodeImageFormat.PNG,
            image_height=200,
            image_width=200,
            resolution=300,
        ),
    )

    response = generate_api.generate_body(generator_params)

    with open(file_name, "wb") as file:
        file.write(response.data)

    print(f"File '{file_name}' generated.")


# Run the main function
if __name__ == "__main__":
    main()
