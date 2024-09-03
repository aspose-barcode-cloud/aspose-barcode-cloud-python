import os
import unittest
import base64

from aspose_barcode_cloud import ApiClient, ScanApi, DecodeBarcodeType, ScanBase64Request
from .load_configuration import TEST_CONFIGURATION


class TestScanBarcode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ScanApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "qr_and_code128.png")
        )

    def test_barcode_scan_get(self):
        """Test case for barcode_scan_get

        Scan barcode from url.
        """

        response = self.api.barcode_scan_get("https://products.aspose.app/barcode/scan/img/how-to/scan/step2.png")

        self.assertEqual(1, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("http://en.m.wikipedia.org", response.barcodes[0].barcode_value)

    def test_barcode_scan_body_post(self):
        """Test case for barcode_scan_body_post
        Scan barcode from an request body.
        Request body should contain data encoded with base64.
        """
        with open(self.test_filename, "rb") as f:
            image_bytes = f.read()
            f.close()

        encoded_string = base64.b64encode(image_bytes).decode()

        response = self.api.barcode_scan_body_post(ScanBase64Request(file_base64=encoded_string))

        self.assertIsNotNone(response and response.barcodes)
        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)

        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)

    def test_barcode_scan_form_post(self):
        """Test case for barcode_scan_form_post

        Recognition of a barcode from file with parameters in form.
        """

        response = self.api.barcode_scan_form_post(open(self.test_filename, "rb"))

        self.assertIsNotNone(response and response.barcodes)
        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)

        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)
