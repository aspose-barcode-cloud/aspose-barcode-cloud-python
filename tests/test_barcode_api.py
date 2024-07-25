import os
import unittest
import uuid

from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    DecodeBarcodeType,
    PresetType,
    GeneratorParamsList,
    GeneratorParams,
    ReaderParams,
    FileApi,
)
from aspose_barcode_cloud.api.barcode_api import BarcodeApi
from .load_configuration import TEST_CONFIGURATION


class TestBarcodeApi(unittest.TestCase):
    """BarcodeApi unit tests"""

    GENERATED_BARCODE_TYPE = EncodeBarcodeType.CODE128
    GENERATED_BARCODE_TEXT = "Hello!"

    @classmethod
    def setUpClass(cls):
        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417Sample.png")
        )

        cls.api_client = ApiClient(configuration=TEST_CONFIGURATION)

        # noinspection PyUnresolvedReferences
        cls.api = BarcodeApi(api_client=cls.api_client)
        cls.temp_folder_path = "BarcodeTests/%s" % uuid.uuid4()
        cls.test_put_barcode_generate_filename = "test_put_barcode_generate_file.png"

    def test_get_barcode_generate(self):
        """Test case for get_barcode_generate

        Generate barcode.
        """
        response = self.api.get_barcode_generate(EncodeBarcodeType.CODE128, "Hello!")

        content_length = int(response.headers["content-length"])
        self.assertGreater(content_length, 0, "content_length=%s" % content_length)
        self.assertEqual("image/png", response.headers["content-type"])

    def test_get_barcode_recognize(self):
        """Test case for get_barcode_recognize

        Recognize barcode from a file on server.
        """
        filename = self.upload_test_file(
            file_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417Sample.png"))
        )

        response = self.api.get_barcode_recognize(
            filename, folder=self.temp_folder_path, preset=PresetType.HIGHPERFORMANCE
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(DecodeBarcodeType.PDF417, barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)

    def test_post_barcode_recognize_from_url_or_content(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode from an url or from request body.
        Request body can contain raw data bytes of the image or encoded with base64.
        """

        response = self.api.post_barcode_recognize_from_url_or_content(
            types=[DecodeBarcodeType.PDF417],
            preset=PresetType.HIGHPERFORMANCE,
            image=self.test_filename,
        )

        self.assertIsNotNone(response and response.barcodes)
        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual("Pdf417", barcode.type)
        self.assertEqual("Aspose.BarCode for Cloud Sample", barcode.barcode_value)
        self.assertGreater(barcode.region[0].x, 0)
        self.assertGreater(barcode.region[0].y, 0)

    def test_post_generate_multiple(self):
        """Test case for post_generate_multiple

        Generate multiple barcodes and return in response stream
        """
        generator_params_list = GeneratorParamsList(
            [
                GeneratorParams(EncodeBarcodeType.CODE128, "First barcode"),
                GeneratorParams(EncodeBarcodeType.QR, "Second barcode"),
            ],
            x_step=0,
            y_step=0,
        )

        response = self.api.post_generate_multiple(generator_params_list)

        content_length = int(response.headers["content-length"])
        self.assertGreater(content_length, 0, "content_length=%s" % content_length)
        self.assertEqual("image/png", response.headers["content-type"])

    def test_put_barcode_generate_file(self):
        """Test case for put_barcode_generate_file

        Generate barcode and save on server (from query params or from file with json or xml content)
        """

        response = self.api.put_barcode_generate_file(
            self.test_put_barcode_generate_filename,
            self.GENERATED_BARCODE_TYPE,
            self.GENERATED_BARCODE_TEXT,
            folder=self.temp_folder_path,
        )

        self.assertGreater(response.file_size, 0)
        self.assertGreater(response.image_width, 0)
        self.assertGreater(response.image_height, 0)

    def test_put_barcode_recognize_from_body(self):
        """Test case for put_barcode_recognize_from_body

        Recognition of a barcode from file on server with parameters in body.
        """

        # Ensure file self.test_put_barcode_generate_filename generated
        self.test_put_barcode_generate_file()

        response = self.api.put_barcode_recognize_from_body(
            self.test_put_barcode_generate_filename,
            ReaderParams(preset=PresetType.HIGHPERFORMANCE),
            folder=self.temp_folder_path,
        )

        self.assertEqual(1, len(response.barcodes))
        barcode = response.barcodes[0]
        self.assertEqual(self.GENERATED_BARCODE_TYPE, barcode.type)
        self.assertEqual(self.GENERATED_BARCODE_TEXT, barcode.barcode_value)

    def test_put_generate_multiple(self):
        """Test case for put_generate_multiple

        Generate image with multiple barcodes and put new file on server
        """
        generator_params_list = GeneratorParamsList(
            [
                GeneratorParams(EncodeBarcodeType.CODE128, "First barcode"),
                GeneratorParams(EncodeBarcodeType.QR, "Second barcode"),
            ],
            x_step=0,
            y_step=0,
        )
        filename = "test_put_generate_multiple.png"

        response = self.api.put_generate_multiple(filename, generator_params_list, folder=self.temp_folder_path)

        self.assertGreater(response.file_size, 0)
        self.assertGreater(response.image_width, 0)
        self.assertGreater(response.image_height, 0)

    def upload_test_file(self, file_path):
        self.assertTrue(os.path.isfile(file_path))
        file_api = FileApi(self.api_client)
        fname = os.path.basename(file_path)

        upload_result = file_api.upload_file(path=self.temp_folder_path + "/" + fname, file=file_path)

        self.assertFalse(upload_result.errors, str(upload_result.errors))
        self.assertTrue(upload_result.uploaded)

        return upload_result.uploaded[0]
