__all__ = ['Beer']

from sqlalchemy import Column, Text

from kordex0.models.meta import Base


class Beer(Base):

    name = Column(Text)
