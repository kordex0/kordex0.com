from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_route('home', '/')
    config.add_route('hello', '/hello/{name}')
    config.add_static_view(name='static', path='kordex0:static')
    config.scan('.views')
    return config.make_wsgi_app()
