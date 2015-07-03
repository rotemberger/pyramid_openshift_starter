from pip.backwardcompat import raw_input

__author__ = 'rotem'
import os
import sys
import transaction
from sqlalchemy import create_engine
from pyramid.paster import get_appsettings, setup_logging
from ..internal.db import DBSession, Base, postgresql_url
from ..models.auth import User


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]

    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = create_engine(postgresql_url(settings))
    DBSession.configure(bind=engine)

    name = raw_input('User name:')
    password = raw_input('Password:')
    permission = raw_input('Permission:')

    with transaction.manager:
        user = User(name=name, password=password, permission=permission)
        DBSession.add(user)
