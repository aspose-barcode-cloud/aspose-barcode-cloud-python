import sys
import unittest
from unittest import mock

from aspose_barcode_cloud import Configuration, ApiClient, GenerateApi, EncodeBarcodeType, EncodeDataType
from aspose_barcode_cloud.rest import RESTClientObject


class TestHeaders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local_config = Configuration(access_token="fake token", host="localhost")
        if sys.version_info.major == 2:
            # For compatibility with Python 2
            cls.assertRegex = cls.assertRegexpMatches

    def setUp(self):
        self.rest_client_mock = mock.Mock(spec_set=RESTClientObject)

    def test_default_headers(self):
        api_client = ApiClient(self.local_config)
        api_client.rest_client = self.rest_client_mock

        GenerateApi(api_client).generate(EncodeBarcodeType.CODE128, EncodeDataType.STRINGDATA, "Test")

        self.assertEqual(1, self.rest_client_mock.GET.call_count)
        headers = self.rest_client_mock.GET.call_args[1]["headers"]
        self.assertEqual("python sdk", headers["x-aspose-client"])
        self.assertRegex(headers["x-aspose-client-version"], r"\d{2}\.\d+\.\d+")
        self.assertRegex(headers["User-Agent"], r"Aspose-Barcode-SDK\/\d{2}.\d+.\d+\/python")

    def test_header_override(self):
        api_client = ApiClient(
            self.local_config,
            header_name="x-aspose-client",
            header_value="some custom sdk",
        )
        api_client.rest_client = self.rest_client_mock

        GenerateApi(api_client).generate(EncodeBarcodeType.CODE128, EncodeDataType.STRINGDATA, "Test")

        self.assertEqual(1, self.rest_client_mock.GET.call_count)
        headers = self.rest_client_mock.GET.call_args[1]["headers"]
        self.assertEqual("some custom sdk", headers["x-aspose-client"])
