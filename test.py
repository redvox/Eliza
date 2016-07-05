#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Testing for Core Module
"""

import unittest
from flask import Flask
from core import metric
from core.start import prepare_app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        app = Flask(__name__)
        app.config.update(
            DEBUG=True,
            SECRET_KEY='secret_key',
            WTF_CSRF_ENABLED=False
        )
        config = prepare_app(app, 'test-app', [], 'local', False, True)
        self.app = app.test_client()
        self.accept_headers = [('Accept', 'application/json')]

    def test_about_page_is_available(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_doc_page_is_available(self):
        response = self.app.get('/doc')
        self.assertEqual(response.status_code, 200)

    def test_status_page_is_available(self):
        response = self.app.get('/unknown/internal/status')
        self.assertEqual(response.status_code, 200)

    def test_status_page_is_available(self):
        response = self.app.get('/unknown/internal/status', headers=self.accept_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')

    def test_metric_add_min(self):
        metric.add_min('add_min', 2)
        self.assertEqual(metric.metrics['add_min'], 2)

        metric.add_min('add_min', 5)
        self.assertEqual(metric.metrics['add_min'], 2)

        metric.add_min('add_min', 1)
        self.assertEqual(metric.metrics['add_min'], 1)

    def test_metric_add_max(self):
        metric.add_max('add_max', 1)
        self.assertEqual(metric.metrics['add_max'], 1)

        metric.add_max('add_max', 5)
        self.assertEqual(metric.metrics['add_max'], 5)

        metric.add_max('add_max', 1)
        self.assertEqual(metric.metrics['add_max'], 5)

    def test_metric_inc(self):
        metric.inc('inc', 1)
        self.assertEqual(metric.metrics['inc'], 1)

        metric.inc('inc', 2)
        self.assertEqual(metric.metrics['inc'], 3)



if __name__ == '__main__':
    unittest.main()


