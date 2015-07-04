__author__ = 'rotem'
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pyramid import testing
from ..internal.auth import hash_password, check_password
from ..models.auth import User


class TestAuthBcrypt(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_passing_password(self):
        hashed = hash_password('topsecret'.encode('utf-8'))
        check = check_password('topsecret'.encode('utf-8'), hashed)
        self.assertTrue(check)

    def test_failing_password(self):
        hashed = hash_password('topsecret'.encode('utf-8'))
        check = check_password('topsecrat'.encode('utf-8'), hashed)
        self.assertFalse(check)


class TestAuthBcryptDB(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

        self.password = "secretpwd".encode()
        self.hashed_password = hash_password(self.password).decode()
        self.user = User(name="secretuser", password=self.hashed_password)
        engine = create_engine('postgresql://develop:develop@127.0.0.1:5432/st4rt3r')
        Session = sessionmaker(bind=engine)

        self.session = Session()
        self.session.add(self.user)
        self.session.commit()

    def tearDown(self):
        self.session.delete(self.user)
        self.session.commit()
        testing.tearDown()

    def test_passing_password(self):
        one = self.session.query(User).filter_by(name="secretuser").one()
        hashed = one.password.encode()
        check = check_password(self.password, hashed)
        self.assertTrue(check)

    def test_failing_password(self):
        one = self.session.query(User).filter_by(name="secretuser").one()
        hashed = one.password.encode()
        check = check_password('topsecraz'.encode(), hashed)
        self.assertFalse(check)
