from pyramid.view import view_config, view_defaults

from kordex0.models import Beer
from kordex0.util.view_util import params
from kordex0.views.base import BaseView

import logging

LOG = logging.getLogger(__name__)


@view_defaults(route_name='hello', renderer='../templates/hello.mako')
class HelloView(BaseView):

    @view_config(route_name='home', renderer='../templates/home.mako')
    def home(self):
        LOG.debug('calling home')
        return {'name': ''}

    @view_config()
    @params
    def hello(self, name):
        LOG.debug('calling hello')
        beer = self.request.dbsession.query(Beer).filter(Beer.name=='Blue Buck').first()
        return {'name': beer.name}
