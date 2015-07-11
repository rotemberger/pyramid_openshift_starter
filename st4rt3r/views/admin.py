__author__ = 'rotem'
from pyramid.view import view_config


@view_config(route_name='admin', request_method='GET', renderer='admin.jinja2', permission='admin')
def admin_page(request):
    return {'project': 'st4rt3r'}