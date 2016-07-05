# -*- coding: utf-8 -*-
import json
import unittest

import os
import requests_mock
from eliza.config import ConfigLoader


@requests_mock.Mocker()
class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.env_HOME = os.environ.get("HOME", "Test Error. Could not read env variable 'HOME'")

    def setUp(self):
        if 'test_env_variable' in os.environ:
            del os.environ['test_env_variable']

    def test_load_config_without_vault(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environment='develop')
        self.assertEqual({'filename': 'develop', 'secret': '', 'test_env': self.env_HOME}, self.config)

    def test_load_config_with_vault(self, mock):
        mock.register_uri('GET', "http://www.some-url.de/v1/secret/path",
                          text=json.dumps({'data': {'value': 'some secret'}}))

        self.config_loader = ConfigLoader(use_vault=True, vault_addr="http://www.some-url.de", vault_token="AAAA")
        self.config = self.config_loader.load_config(path='resources/', environment='develop')
        self.assertEqual({'filename': 'develop', 'secret': 'some secret', 'test_env': self.env_HOME}, self.config)
