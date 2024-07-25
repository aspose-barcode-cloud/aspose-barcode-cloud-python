import os
import sys
import unittest
import pathlib

from aspose_barcode_cloud import PresetType, ApiClient, BarcodeApi, DecodeBarcodeType
from .load_configuration import TEST_CONFIGURATION


PY35orLess = sys.version_info[0:2] <= (3, 5)


class TestRecognizeFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417Sample.png")
        )

        cls.api = BarcodeApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

    def test_post_barcode_recognize_from_url_or_content_filename(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from a local file.
        """

        response = self.api.post_barcode_recognize_from_url_or_content(
            preset=PresetType.HIGHPERFORMANCE, image=self.test_filename, types=[DecodeBarcodeType.PDF417]
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)

    @unittest.skipIf(PY35orLess, "No pathlib in Python2 and Python3.5 raises an error")
    def test_post_barcode_recognize_from_url_or_content_pathlike(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from a local file by pathlike.
        """

        response = self.api.post_barcode_recognize_from_url_or_content(
            preset=PresetType.HIGHPERFORMANCE, image=pathlib.Path(self.test_filename), types=[DecodeBarcodeType.PDF417]
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)

    def test_post_barcode_recognize_from_url_or_content_file_obj(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from a local file obj.
        """
        with open(self.test_filename, "rb") as file_obj:
            response = self.api.post_barcode_recognize_from_url_or_content(
                preset=PresetType.HIGHPERFORMANCE, image=file_obj, types=[DecodeBarcodeType.PDF417]
            )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)
