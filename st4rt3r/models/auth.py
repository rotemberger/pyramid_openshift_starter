from pyramid.security import Allow
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import Column, Integer, String
from ..internal.db import Base, DBSession


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


def groupfinder(userid, request):
    try:
        user = DBSession.query(User).filter(User.name == userid).one()
        return [user.permission]
    except NoResultFound:
        return None
