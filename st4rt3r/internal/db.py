__author__ = 'rotem'
from .openshift import Environ


def postgresql_url(settings):
    env = Environ(settings)
    user = env.get('OPENSHIFT_POSTGRESQL_DB_USERNAME')
    password = env.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD')
    host = env.get('OPENSHIFT_POSTGRESQL_DB_HOST')
    port = env.get('OPENSHIFT_POSTGRESQL_DB_PORT')
    db = env.get('PGDATABASE')
    url = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, db)
    return url
