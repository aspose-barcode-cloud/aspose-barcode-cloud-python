import os
from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    EncodeDataType,
    EncodeData,
    GenerateParams,
    BarcodeImageParams,
    BarcodeImageFormat,
    GraphicsUnit,
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
    # Define the output file path
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417.png"))

    # Create API client and generate parameters
    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    generate_api = GenerateApi(api_client=api_client)

    generate_params = GenerateParams(
        EncodeBarcodeType.PDF417,
        EncodeData(data="Aspose.BarCode.Cloud"),
        BarcodeImageParams(
            image_format=BarcodeImageFormat.PNG, image_height=2, image_width=3, resolution=96, units=GraphicsUnit.INCH
        ),
    )

    # Generate barcode and save to file
    response = generate_api.generate_body(generate_params)
    with open(file_name, "wb") as file:
        file.write(response.data)

    print(f"File '{file_name}' generated.")


# Entry point for async execution
if __name__ == "__main__":
    main()
