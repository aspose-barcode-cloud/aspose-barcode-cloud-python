import os
from aspose_barcode_cloud import (
    ApiClient,
    GenerateApi,
    EncodeBarcodeType,
    BarcodeImageFormat,
    Configuration
)

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

async def main():
    file_name = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),  # Current file directory
        "..", "..", "..", "..", "Code39.png"  # Going up 4 directories and adding Code39.png
    )

    api_client = ApiClient(configuration=make_configuration())
    generate_api = GenerateApi(api_client=api_client)

    request_params = {
        'encode_barcode_type': EncodeBarcodeType.CODE39,
        'text': "Aspose",
        'foreground_color': "Green",
        'background_color': "Yellow",
        'image_format': BarcodeImageFormat.GIF
    }

    # Generate barcode
    response = await generate_api.barcode_generate_multipart_post(request_params)

    # Write to file
    with open(file_name, 'wb') as stream:
        stream.write(response.data)

    print(f"File '{file_name}' generated.")

if __name__ == "__main__":
    main()
