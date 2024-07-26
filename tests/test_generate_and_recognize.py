import os
import tempfile
import unittest

from aspose_barcode_cloud import (
    BarcodeApi,
    ApiClient,
    EncodeBarcodeType,
    PresetType,
    DecodeBarcodeType,
)
from .load_configuration import TEST_CONFIGURATION


class TestGenerateAndRecognize(unittest.TestCase):
    api_client = None
    api = None

    @classmethod
    def setUpClass(cls):
        cls.api_client = ApiClient(TEST_CONFIGURATION)
        cls.api = BarcodeApi(cls.api_client)

    def test_generate_and_recognize(self):
        generated = self.api.get_barcode_generate(EncodeBarcodeType.QR, "Should recognize this")
        self.assertGreater(len(generated.data), 0)

        fd, temp_filename = tempfile.mkstemp()
        os.close(fd)
        try:
            with open(temp_filename, "wb") as f:
                f.write(generated.data)

            recognized = self.api.post_barcode_recognize_from_url_or_content(
                image=temp_filename, preset=PresetType.HIGHPERFORMANCE, types=[DecodeBarcodeType.QR]
            )
        finally:
            os.remove(temp_filename)

        self.assertIsNotNone(recognized and recognized.barcodes)
        self.assertEqual(1, len(recognized.barcodes))
        barcode = recognized.barcodes[0]
        self.assertEqual(DecodeBarcodeType.QR, barcode.type)
        self.assertEqual("Should recognize this", barcode.barcode_value)
