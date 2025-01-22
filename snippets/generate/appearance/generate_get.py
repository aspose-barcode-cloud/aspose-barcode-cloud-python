import os
from aspose_barcode_cloud import ApiClient, EncodeBarcodeType, BarcodeImageFormat, CodeLocation, Configuration
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
    configuration = make_configuration()
    api_client = ApiClient(configuration=configuration)
    generate_api = GenerateApi(api_client=api_client)

    response = generate_api.generate(
        EncodeBarcodeType.QR,
        "Aspose.BarCode.Cloud",
        image_format=BarcodeImageFormat.PNG,
        foreground_color="Black",
        background_color="White",
        resolution=300,
        image_height=200,
        image_width=200,
        text_location=CodeLocation.BELOW,
    )

    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "qr.png"))

    with open(file_name, "wb") as file:
        file.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
