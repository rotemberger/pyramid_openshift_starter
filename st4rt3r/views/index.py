from pyramid.view import view_config


@view_config(route_name='index', renderer='index.jinja2')
def index_page(request):
    return {'project': 'st4rt3r'}
