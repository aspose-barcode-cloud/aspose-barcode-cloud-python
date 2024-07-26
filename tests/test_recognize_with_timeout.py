import json
import os
import re
import unittest

from aspose_barcode_cloud import ApiClient, BarcodeApi, ApiException
from .load_configuration import TEST_CONFIGURATION


class TestRecognizeWithTimeout(unittest.TestCase):
    EXPECTED_MESSAGE_RE = re.compile(
        r"^Try reducing the image size to avoid the timeout\. Recognition is aborted\. Execution time: \d+ ms\.$"
    )

    @classmethod
    def setUpClass(cls):
        cls.api = BarcodeApi(api_client=ApiClient(configuration=TEST_CONFIGURATION))

        cls.test_filename = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "testdata", "pdf417Sample.png")
        )

    def test_post_barcode_recognize_from_url_or_content(self):
        """Test case for post_barcode_recognize_from_url_or_content

        Recognize barcode with timeout.
        """

        with self.assertRaises(ApiException) as context:
            self.api.post_barcode_recognize_from_url_or_content(
                image=self.test_filename,
                timeout=1,
            )
        self.assertEqual(408, context.exception.status)
        message = json.loads(context.exception.body)["error"]["message"]
        self.assertTrue(
            self.EXPECTED_MESSAGE_RE.match(message),
            msg="'%s' doesn't match '%s'" % (message, self.EXPECTED_MESSAGE_RE.pattern),
        )
