import os
import unittest

from aspose_barcode_cloud import ApiClient, BarcodeApi, DecodeBarcodeType, ChecksumValidation
from .load_configuration import TEST_CONFIGURATION


class TestScanBarcode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = BarcodeApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

    @staticmethod
    def expand_test_filename(short_filename: str):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", short_filename))

    def test_scan_barcode(self):
        """Test case for scan_barcode

        Scan barcode.
        """

        response = self.api.scan_barcode(
            self.expand_test_filename("qr_and_code128.png"),
            decode_types=[DecodeBarcodeType.CODE128, DecodeBarcodeType.QR],
        )

        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)

        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)

    def test_scan_code39(self):
        """Test case for scan_barcode

        Scan Code39.
        """

        response = self.api.scan_barcode(
            self.expand_test_filename("Code39.jpg"),
            decode_types=[DecodeBarcodeType.CODE39EXTENDED],
            checksum_validation=ChecksumValidation.OFF,
        )

        self.assertEqual(1, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.CODE39EXTENDED, response.barcodes[0].type)
        self.assertEqual("8M93", response.barcodes[0].barcode_value)
