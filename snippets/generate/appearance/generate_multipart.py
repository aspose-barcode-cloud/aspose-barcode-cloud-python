import os
from aspose_barcode_cloud import ApiClient, EncodeBarcodeType, BarcodeImageFormat, CodeLocation, Configuration
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
    file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417.svg"))

    api_client = ApiClient(configuration=make_configuration())
    generate_api = GenerateApi(api_client=api_client)

    # Generate barcode
    response = generate_api.generate_multipart(
        barcode_type=EncodeBarcodeType.PDF417,
        data="Aspose.BarCode.Cloud",
        text_location=CodeLocation.ABOVE,
        image_format=BarcodeImageFormat.SVG,
    )

    with open(file_name, "wb") as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    main()
