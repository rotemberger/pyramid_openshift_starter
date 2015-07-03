__author__ = 'rotem'
from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

import unittest
from pyramid import testing
from ..internal.db import postgresql_url, DBSession, Base


class Tester(Base):
        __tablename__ = 'tester'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))


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


class TestPostgresqlQuery(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.settings = {
            'openshift.PGDATABASE': 'st4rt3r',
            'openshift.OPENSHIFT_POSTGRESQL_DB_USERNAME': 'develop',
            'openshift.OPENSHIFT_POSTGRESQL_DB_PASSWORD': 'develop',
            'openshift.OPENSHIFT_POSTGRESQL_DB_HOST': '127.0.0.1',
            'openshift.OPENSHIFT_POSTGRESQL_DB_PORT': '5432'
        }

        self.metadata = MetaData()

        self.tester = Table('tester', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(16), nullable=False)
        )

        self.engine = create_engine(postgresql_url(self.settings))
        self.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        tester = Tester(name="test0")
        self.session.add(tester)
        self.session.commit()

    def tearDown(self):
        testing.tearDown()
        self.session.close()
        self.metadata.drop_all(self.engine)

    def test_existing_entry(self):
        result = self.session.query(Tester).filter_by(name="test0").one()
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, "test0")

    def test_non_existing_entry(self):
        one = self.session.query(Tester).filter_by(name="test1").one

        self.assertRaises(NoResultFound, one)
