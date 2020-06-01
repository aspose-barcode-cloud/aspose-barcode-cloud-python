import unittest

from aspose_barcode_cloud import Configuration


class TestConfiguration(unittest.TestCase):
    def test_token_url(self):
        config = Configuration(token_url="token url")
        self.assertEqual("token url", config.token_url)


if __name__ == '__main__':
    unittest.main()
