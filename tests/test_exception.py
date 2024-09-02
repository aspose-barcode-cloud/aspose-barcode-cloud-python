import os
import unittest
import uuid
from typing import cast

from aspose_barcode_cloud import (
    ApiClient,
    EncodeBarcodeType,
    ApiException,
    ApiErrorResponse,
)
from aspose_barcode_cloud.api.generate_api import GenerateApi
from .load_configuration import TEST_CONFIGURATION


class TestException(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.api_client = ApiClient(configuration=TEST_CONFIGURATION)

        # noinspection PyUnresolvedReferences
        cls.api = GenerateApi(api_client=cls.api_client)

    def test_exception_message_parsed(self):

        thrown = False
        try:
            self.api.generate(EncodeBarcodeType.CODE128, "")
        except ApiException as e:
            thrown = True
            print(e)
            self.assertEqual(400, e.status)
            self.assertEqual("Bad Request", e.reason)
            self.assertTrue(b"Error: Field name: 'Data' errors: The Data field is required." in e.body)

        self.assertTrue(thrown)


if __name__ == "__main__":
    unittest.main()
