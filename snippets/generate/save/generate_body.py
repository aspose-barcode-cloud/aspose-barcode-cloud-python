import os
from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    EncodeDataType,
    EncodeData,
    GenerateParams,
    BarcodeImageParams,
    BarcodeImageFormat,
    Configuration,
)
from aspose_barcode_cloud.api.generate_api import GenerateApi


def make_configuration():
    env_token = os.getenv("TEST_CONFIGURATION_ACCESS_TOKEN")
    if env_token:
        config = Configuration(access_token=env_token)
    else:
        config = Configuration(
            client_id="Client Id from https://dashboard.aspose.cloud/applications",
            client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
        )
    return config


def main():
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417.png"))

    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    generate_api = GenerateApi(api_client=api_client)

    generate_params = GenerateParams(
        barcode_type=EncodeBarcodeType.PDF417,
        encode_data=EncodeData(data_type=EncodeDataType.STRINGDATA, data="Aspose.BarCode.Cloud"),
        barcode_image_params=BarcodeImageParams(
            foreground_color="#FF5733",
            background_color="#FFFFFF",
            image_format=BarcodeImageFormat.JPEG,
        ),
    )

    response = generate_api.generate_body(generate_params)

    with open(file_name, "wb") as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
