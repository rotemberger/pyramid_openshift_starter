__author__ = 'rotem'
import unittest
from pyramid import testing
from ..internal.openshift import Environ, EnvironException


class TestEnviron(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.env = Environ({
            'openshift.PGDATABASE': 'tester',
            'openshift.OPENSHIFT_REPO_DIR': 'repo/dir',
            'openshift.OPENSHIFT_DATA_DIR': '/data/dir',
            'openshift.OPENSHIFT_POSTGRESQL_DB_USERNAME': 'develop',
            'openshift.OPENSHIFT_POSTGRESQL_DB_PASSWORD': 'develop',
            'openshift.OPENSHIFT_POSTGRESQL_DB_HOST': '127.0.0.1',
            'openshift.OPENSHIFT_POSTGRESQL_DB_PORT': '5432'
        })

    def tearDown(self):
        testing.tearDown()

    def test_passing_key(self):
        self.assertEqual(self.env.get('PGDATABASE'), 'tester')
        self.assertEqual(self.env.get('OPENSHIFT_REPO_DIR'), 'repo/dir')
        self.assertEqual(self.env.get('OPENSHIFT_DATA_DIR'), '/data/dir')
        self.assertEqual(self.env.get('OPENSHIFT_POSTGRESQL_DB_USERNAME'), 'develop')
        self.assertEqual(self.env.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD'), 'develop')
        self.assertEqual(self.env.get('OPENSHIFT_POSTGRESQL_DB_HOST'), '127.0.0.1')
        self.assertEqual(self.env.get('OPENSHIFT_POSTGRESQL_DB_PORT'), '5432')

    def test_failing_key(self):
        self.assertRaises(EnvironException, self.env.get, 'DUMMY_KEY')
