from sqlalchemy import engine_from_config
from sqlalchemy.orm import configure_mappers, sessionmaker

# import or define all models here to ensure they are attached to the
# Base.metadata prior to any initialization routines
from kordex0.models.meta import Base
from .drink import *

# run configure_mappers after defining all of the models to ensure
# all relationships can be setup
configure_mappers()

def includeme(config):
    settings = config.get_settings()
    engine = engine_from_config(settings, 'sqlalchemy.')
    factory = sessionmaker()
    factory.configure(bind=engine)
    Base.metadata.create_all(engine)
    config.add_request_method(lambda r: factory(), 'dbsession', reify=True)
    return config
