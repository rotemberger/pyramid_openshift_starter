from pyramid.view import view_config


@view_config(route_name='home', renderer='st4rt3r:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'st4rt3r'}
