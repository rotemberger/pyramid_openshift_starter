__author__ = 'rotem'
from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember
from sqlalchemy.orm.exc import NoResultFound
from ..internal.db import DBSession
from ..models.auth import User


@view_config(route_name='login', request_method="GET", renderer="login.jinja2")
@forbidden_view_config(renderer="login.jinja2")
def login_page(request):
    return {'project': 'st4rt3r'}


@view_config(route_name='login', request_method='POST', xhr='true', renderer='json')
def login_xhr(request):
    username = request.json_body.get('username')
    password = request.json_body.get('password')
    try:
        user = DBSession.query(User).filter(User.name == username).one()
        if user.password == password:
            headers = remember(request, username)
            response = request.response
            response.headerlist.extend(headers)
            return {'status': 'success'}
    except NoResultFound:
        pass

    return {'status': 'fail', 'msg': 'Bad user name or password.'}
