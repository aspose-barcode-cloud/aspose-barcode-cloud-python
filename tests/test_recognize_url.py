import unittest

from aspose_barcode_cloud import PresetType, ApiClient, BarcodeApi, DecodeBarcodeType
from .load_configuration import TEST_CONFIGURATION


class TestRecognizeUrl(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_url = "https://products.aspose.app/barcode/scan/img/how-to/scan/step2.png"

        cls.api = BarcodeApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

    def test_post_barcode_recognize_from_url_or_content_bytes(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from URL.
        """

        response = self.api.post_barcode_recognize_from_url_or_content(
            preset=PresetType.HIGHPERFORMANCE, url=self.test_url, types=[DecodeBarcodeType.QR]
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.QR, barcode.type)
        self.assertEqual("http://en.m.wikipedia.org", barcode.barcode_value)
