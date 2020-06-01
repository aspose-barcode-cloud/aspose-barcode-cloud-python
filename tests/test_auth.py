import os
import unittest

from aspose_barcode_cloud import Configuration, ApiClient, BarcodeApi, EncodeBarcodeType

CONFIG_FILENAME = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'configuration.qa.json')


@unittest.skipUnless(os.path.exists(CONFIG_FILENAME), "Requested file '%s' does not exist" % CONFIG_FILENAME)
class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Configuration.from_file(CONFIG_FILENAME)
        cls.api_client = ApiClient(cls.config)
        cls.api = BarcodeApi(cls.api_client)

    def test_access_token(self):
        self.assertIsNone(self.config._access_token)
        token = self.config.access_token
        self.assertTrue(token, "Token=%s" % token)

    def test_access_token_raises(self):
        config = Configuration()
        with self.assertRaises(ValueError) as cm:
            token = config.access_token
        the_exception = cm.exception
        self.assertEqual("No access token or app_sid and app_key specified", the_exception.args[0])

    def test_works_with_access_token(self):
        api = BarcodeApi(ApiClient(Configuration(access_token=self.config.access_token, host=self.config.host)))
        response = api.get_barcode_generate(EncodeBarcodeType.QR, "Testing")
        self.assertEqual(200, response.status)

    def test_unauthorized_raises(self):
        api = BarcodeApi(ApiClient(Configuration(access_token="incorrect token")))

        with self.assertRaises(Exception) as context:
            api.get_barcode_generate(EncodeBarcodeType.QR, "Testing")

        self.assertEqual(400, context.exception.status)


if __name__ == '__main__':
    unittest.main()
