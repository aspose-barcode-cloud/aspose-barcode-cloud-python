import unittest

from aspose_barcode_cloud import (
    Configuration,
    ApiClient,
    GenerateApi,
    EncodeBarcodeType,
    EncodeDataType,
    ApiException,
)
from .load_configuration import TEST_CONFIGURATION


@unittest.skipUnless(
    TEST_CONFIGURATION._client_id and TEST_CONFIGURATION._client_secret,
    "No client_id and client_secret provided",
)
class TestAuth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_client = ApiClient(TEST_CONFIGURATION)
        cls.api = GenerateApi(cls.api_client)

    def test_access_token(self):
        self.assertIsNone(TEST_CONFIGURATION._access_token)
        token = TEST_CONFIGURATION.access_token
        self.assertTrue(token, "Token=%s" % token)

    def test_access_token_raises(self):
        config = Configuration()
        with self.assertRaises(ValueError) as cm:
            _ = config.access_token
        the_exception = cm.exception
        self.assertEqual(
            "No access_token or client_id and client_secret specified",
            the_exception.args[0],
        )

    def test_works_with_access_token(self):
        api = GenerateApi(
            ApiClient(
                Configuration(
                    access_token=TEST_CONFIGURATION.access_token,
                    host=TEST_CONFIGURATION.host,
                )
            )
        )

        response = api.generate(EncodeBarcodeType.QR, "Testing", EncodeDataType.STRINGDATA)
        self.assertEqual(200, response.status)

    def test_unauthorized_raises(self):
        api = GenerateApi(ApiClient(Configuration(access_token="incorrect token", host=TEST_CONFIGURATION.host)))

        with self.assertRaises(ApiException) as context:
            api.generate(EncodeBarcodeType.QR, "Testing", EncodeDataType.STRINGDATA)

        self.assertEqual(401, context.exception.status)
