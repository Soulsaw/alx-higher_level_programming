#!/usr/bin/python3
"""The SQL definition of the base class
"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """This class map the State tables
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
