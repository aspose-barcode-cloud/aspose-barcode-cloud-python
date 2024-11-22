
import os
import asyncio
from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    EncodeDataType,
    EncodeData,
    GenerateParams,
    Configuration,
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


def main():
    file_name = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Pdf417.png")

    config = make_configuration()
    api_client = ApiClient(configuration=config)
    generate_api = GenerateApi(api_client=api_client)

    post_params = GenerateParams(
        BarcodeType=EncodeBarcodeType.PDF417,
        EncodeData=EncodeData(
            DataType=EncodeDataType.BASE64BYTES,
            Data="QXNwb3NlLkJhckNvZGUuQ2xvdWQ="
        )
    )

    # Generate barcode
    response = generate_api.barcode_generate_body_post(post_params)

    # Save image to file
    with open(file_name, 'wb') as file:
        file.write(response.data)

    print(f"File '{file_name}' generated.")


if __name__ == "__main__":
    asyncio.run(main())
