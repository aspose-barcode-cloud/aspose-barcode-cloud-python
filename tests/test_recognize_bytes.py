import io
import os
import unittest

from aspose_barcode_cloud import PresetType, ApiClient, BarcodeApi, DecodeBarcodeType
from .load_configuration import TEST_CONFIGURATION


class TestRecognizeBytes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417Sample.png")
        )

        cls.api = BarcodeApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

    def test_post_barcode_recognize_from_url_or_content_bytes(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from bytes.
        """
        with open(self.test_filename, "rb") as f:
            image_bytes = f.read()

        response = self.api.post_barcode_recognize_from_url_or_content(
            preset=PresetType.HIGHPERFORMANCE, image=image_bytes, types=[DecodeBarcodeType.PDF417]
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)

    def test_post_barcode_recognize_from_url_or_content_bytearray(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from bytes.
        """
        with open(self.test_filename, "rb") as f:
            image_bytes = bytearray(f.read())

        response = self.api.post_barcode_recognize_from_url_or_content(
            preset=PresetType.HIGHPERFORMANCE, image=image_bytes, types=[DecodeBarcodeType.PDF417]
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)

    def test_post_barcode_recognize_from_url_or_content_BytesIO(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from BytesIO.
        """
        with open(self.test_filename, "rb") as f:
            bytes_io = io.BytesIO(f.read())

        response = self.api.post_barcode_recognize_from_url_or_content(
            preset=PresetType.HIGHPERFORMANCE, image=bytes_io, types=[DecodeBarcodeType.PDF417]
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)
