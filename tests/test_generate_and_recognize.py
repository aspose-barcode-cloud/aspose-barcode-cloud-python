import os
import tempfile
import unittest

from aspose_barcode_cloud import (
    GenerateApi,
    RecognizeApi,
    ApiClient,
    EncodeBarcodeType,
    DecodeBarcodeType,
    EncodeDataType,
)
from .load_configuration import TEST_CONFIGURATION


class TestGenerateAndRecognize(unittest.TestCase):
    api_client = None
    generateApi = None
    recognizeApi = None

    @classmethod
    def setUpClass(cls):
        cls.api_client = ApiClient(TEST_CONFIGURATION)
        cls.generateApi = GenerateApi(cls.api_client)
        cls.recognizeApi = RecognizeApi(cls.api_client)

    def test_generate_and_recognize(self):
        generated = self.generateApi.generate(EncodeBarcodeType.QR, "Should recognize this")
        self.assertGreater(len(generated.data), 0)

        fd, temp_filename = tempfile.mkstemp()
        os.close(fd)
        try:
            with open(temp_filename, "wb") as fw:
                fw.write(generated.data)

            with open(temp_filename, "rb") as fr:
                recognized = self.recognizeApi.recognize_multipart(DecodeBarcodeType.QR, fr)

        finally:
            os.remove(temp_filename)

        self.assertIsNotNone(recognized and recognized.barcodes)
        self.assertEqual(1, len(recognized.barcodes))
        barcode = recognized.barcodes[0]
        self.assertEqual(DecodeBarcodeType.QR, barcode.type)
        self.assertEqual("Should recognize this", barcode.barcode_value)
