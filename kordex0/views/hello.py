from pyramid.view import view_config, view_defaults

from kordex0.util.view_util import params
from kordex0.views.base import BaseView


@view_defaults(route_name='hello', renderer='../templates/hello.mako')
class HellotView(BaseView):

    @view_config(route_name='home', renderer='../templates/home.mako')
    def home(self):
        return {'name': ''}

    @view_config()
    @params
    def hello(self, name):
        return {'name': name}
