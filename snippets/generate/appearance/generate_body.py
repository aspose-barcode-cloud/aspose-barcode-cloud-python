import os
from aspose_barcode_cloud import (
    ApiClient,
    Configuration,
    EncodeBarcodeType,
    EncodeDataType,
    EncodeData,
    GenerateParams,
    BarcodeImageParams,
    BarcodeImageFormat,
)
from aspose_barcode_cloud.api.generate_api import GenerateApi

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

# Main function to generate barcode
def main():
    # Set up the configuration and API client
    configuration = make_configuration()
    api_client = ApiClient(configuration)
    generate_api = GenerateApi(api_client=api_client)

    # Define the file path for the generated barcode
    file_name = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        "..", "testdata", "code39.jpeg"))

    # Set up the generation parameters
    generate_params = GenerateParams(
        barcode_type=EncodeBarcodeType.CODE39,
        encode_data=EncodeData(data="Aspose", data_type=EncodeDataType.STRINGDATA),
        barcode_image_params=BarcodeImageParams(
            foreground_color="#FF0000",
            background_color="#FFFF00",
            image_format=BarcodeImageFormat.JPEG,
            rotation_angle=90
        )
    )

    # Generate barcode
    response = generate_api.generate_body(generate_params)

    # Save the generated image to a file
    with open(file_name, 'wb') as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")

# To run the main function if this script is executed
if __name__ == "__main__":
    main()
