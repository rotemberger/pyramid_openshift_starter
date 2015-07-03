from pyramid.config import Configurator
from sqlalchemy import create_engine
from .internal.db import DBSession, Base, postgresql_url


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = create_engine(postgresql_url(settings))
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
