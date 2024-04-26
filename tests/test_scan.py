from __future__ import absolute_import, division

import os
import unittest

from aspose_barcode_cloud import ApiClient, BarcodeApi, DecodeBarcodeType
from .load_configuration import TEST_CONFIGURATION


class TestScanBarcode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = BarcodeApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "qr_and_code128.png")
        )

    def test_scan_barcode(self):
        """Test case for scan_barcode

        Scan barcode.
        """

        response = self.api.scan_barcode(
            self.test_filename, decode_types=[DecodeBarcodeType.CODE128, DecodeBarcodeType.QR]
        )

        self.assertEqual(2, len(response.barcodes))

        self.assertEqual(DecodeBarcodeType.QR, response.barcodes[0].type)
        self.assertEqual("QR text", response.barcodes[0].barcode_value)

        self.assertEqual(DecodeBarcodeType.CODE128, response.barcodes[1].type)
        self.assertEqual("Code128 text", response.barcodes[1].barcode_value)
