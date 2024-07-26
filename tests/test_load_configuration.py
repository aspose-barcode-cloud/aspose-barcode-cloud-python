import os
import unittest
import uuid

from . import load_configuration


class TestLoadConfiguration(unittest.TestCase):
    def setUp(self):
        self.uniq_prefix = uuid.uuid4()

    def test_load_from_file(self):
        file_name = os.path.join(os.path.split(os.path.abspath(__file__))[0], "configuration.example.json")
        config = load_configuration.from_file(file_name)

        self.assertEqual("JWT token", config.access_token)
        self.assertEqual("https://api.aspose.cloud/v3.0", config.host)
        self.assertEqual("https://api.aspose.cloud/connect/token", config.token_url)

    def test_load_from_env(self):
        os.environ["%s_ACCESS_TOKEN" % self.uniq_prefix] = "Access Token"
        config = load_configuration.from_env(self.uniq_prefix)

        self.assertEqual("Access Token", config.access_token)
