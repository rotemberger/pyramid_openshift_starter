__author__ = 'rotem'
import unittest
from pyramid import testing
from ..internal.db import postgresql_url


class TestPostgresqlUrl(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.settings = {
            'openshift.PGDATABASE': 'st4rt3r',
            'openshift.OPENSHIFT_POSTGRESQL_DB_USERNAME': 'develop',
            'openshift.OPENSHIFT_POSTGRESQL_DB_PASSWORD': 'develop',
            'openshift.OPENSHIFT_POSTGRESQL_DB_HOST': '127.0.0.1',
            'openshift.OPENSHIFT_POSTGRESQL_DB_PORT': '5432'
        }

    def tearDown(self):
        testing.tearDown()

    def test_passing_url(self):
        url = postgresql_url(self.settings)
        self.assertEqual(url, 'postgresql://develop:develop@127.0.0.1:5432/st4rt3r')

