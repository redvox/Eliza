# -*- coding: utf-8 -*-
import json
import unittest

import os
import requests_mock
from eliza import errors
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

    def test_load_config(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environments='develop')
        self.assertEqual({'filename': 'develop'}, self.config)

    def test_load_multiple_configs(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environments=['develop', 'live'])
        self.assertEqual({'filename': 'live'}, self.config)

    def test_load_multiple_configs_with_empty_files(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environments=['develop', 'empty', 'live'])
        self.assertEqual({'filename': 'live'}, self.config)

    def test_load_config_with_env_variable(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environments='env')
        self.assertEqual({'filename': 'env', 'test_env': self.env_HOME, 'empty_test_env': ''}, self.config)

    def test_load_config_with_vault(self, mock):
        mock.register_uri('GET', "http://www.some-url.de/v1/secret/path",
                          text=json.dumps({'data': {'value': 'some secret'}}))

        self.config_loader = ConfigLoader(use_vault=True, vault_addr="http://www.some-url.de", vault_token="AAAA")
        self.config = self.config_loader.load_config(path='resources/', environments='vault')
        self.assertEqual({'filename': 'vault', 'secret': 'some secret'}, self.config)

    def test_load_config_with_vault_disabled(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environments='vault')
        self.assertEqual({'filename': 'vault', 'secret': ''}, self.config)

    def test_load_config_fill_with_defaults(self, _):
        self.config_loader = ConfigLoader(use_vault=False)
        self.config = self.config_loader.load_config(path='resources/', environments='with_defaults',
                                                     fill_with_defaults=True)
        expected = {
            'defaults': {
                'config': {
                    'protocol': 'http',
                    'api': '/v2/apps',
                    'username': 'username',
                    'password': 'password'}},
            'config': [{'api': '/v2/apps',
                        'password': 'password',
                        'protocol': 'ftp',
                        'username': 'username'},
                       {'api': '/v2/apps',
                        'host': 'marathon.tesla.develop.lhotse.ov.otto.de',
                        'password': 'password',
                        'protocol': 'http',
                        'username': 'username'},
                       {'api': '/v2/apps',
                        'password': 'doe',
                        'protocol': 'http',
                        'username': 'john'}]
        }
        self.assertDictEqual(expected, self.config)
