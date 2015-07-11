from pyramid.security import Allow
from sqlalchemy import Column, Integer, String
from ..internal.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(256))
    permission = Column(String(50))


class RootFactory(object):
    __acl__ = [(Allow, 'admin', 'admin')]

    def __init__(self, request):
        pass
