import os
import tempfile
import unittest

from aspose_barcode_cloud import Configuration, BarcodeApi, ApiClient, EncodeBarcodeType, PresetType, DecodeBarcodeType


class TestGenerateAndRecognize(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Configuration.from_file(os.path.join(os.path.split(os.path.abspath(__file__))[0],
                                                          'configuration.json'))
        cls.api_client = ApiClient(cls.config)
        cls.api = BarcodeApi(cls.api_client)

    def test_generate_and_recognize(self):
        generated = self.api.get_barcode_generate(EncodeBarcodeType.QR, "Should recognize this")
        self.assertGreater(len(generated.data), 0)

        temp_filename = tempfile.mktemp()
        try:
            with open(temp_filename, 'wb') as f:
                f.write(generated.data)

            recognized = self.api.post_barcode_recognize_from_url_or_content(
                image=temp_filename,
                preset=PresetType.HIGHPERFORMANCE)
        finally:
            os.remove(temp_filename)

        self.assertEqual(1, len(recognized.barcodes))
        barcode = recognized.barcodes[0]
        self.assertEqual(DecodeBarcodeType.QR, barcode.type)
        self.assertEqual("Should recognize this", barcode.barcode_value)


if __name__ == '__main__':
    unittest.main()
