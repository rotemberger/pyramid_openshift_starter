from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import create_engine
from .internal.db import DBSession, Base, postgresql_url
from .models.auth import groupfinder, RootFactory
from .routes import mapping


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = create_engine(postgresql_url(settings))
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings, root_factory=RootFactory)

    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    for route, name in mapping.items():
        config.add_route(name, route)
    config.scan()
    return config.make_wsgi_app()
