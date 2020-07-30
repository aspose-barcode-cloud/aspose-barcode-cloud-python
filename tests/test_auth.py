from __future__ import absolute_import, division

import unittest

from aspose_barcode_cloud import Configuration, ApiClient, BarcodeApi, EncodeBarcodeType
from .load_configuration import TEST_CONFIGURATION


@unittest.skipUnless(TEST_CONFIGURATION._app_sid and TEST_CONFIGURATION._app_key, "No app_sid and app_key provided")
class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_client = ApiClient(TEST_CONFIGURATION)
        cls.api = BarcodeApi(cls.api_client)

    def test_access_token(self):
        self.assertIsNone(TEST_CONFIGURATION._access_token)
        token = TEST_CONFIGURATION.access_token
        self.assertTrue(token, "Token=%s" % token)

    def test_access_token_raises(self):
        config = Configuration()
        with self.assertRaises(ValueError) as cm:
            token = config.access_token
        the_exception = cm.exception
        self.assertEqual("No access_token or app_sid and app_key specified", the_exception.args[0])

    def test_works_with_access_token(self):
        api = BarcodeApi(ApiClient(Configuration(access_token=TEST_CONFIGURATION.access_token, host=TEST_CONFIGURATION.host)))
        response = api.get_barcode_generate(EncodeBarcodeType.QR, "Testing")
        self.assertEqual(200, response.status)

    def test_unauthorized_raises(self):
        api = BarcodeApi(ApiClient(Configuration(access_token="incorrect token")))

        with self.assertRaises(Exception) as context:
            api.get_barcode_generate(EncodeBarcodeType.QR, "Testing")

        self.assertEqual(400, context.exception.status)


if __name__ == '__main__':
    unittest.main()
