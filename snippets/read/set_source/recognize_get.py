from aspose_barcode_cloud import ApiClient, Configuration, RecognizeApi, DecodeBarcodeType


def main():
    config = Configuration(
        client_id="Client Id from https://dashboard.aspose.cloud/applications",
        client_secret="Client Secret from https://dashboard.aspose.cloud/applications",
    )
    recognize_api = RecognizeApi(ApiClient(config))

    # Call the API to recognize the barcode
    result = recognize_api.recognize(
        barcode_type=DecodeBarcodeType.QR, file_url="https://products.aspose.app/barcode/scan/img/how-to/scan/step2.png"
    )

    # Output the result
    if result.barcodes:
        print(f"File recognized, result: '{result.barcodes[0].barcode_value}'")
    else:
        print("No barcodes were recognized.")


if __name__ == "__main__":
    main()
