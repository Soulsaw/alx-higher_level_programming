#!/usr/bin/python3
"""The SQL definition of the base class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """This class map the State tables
    """
    __tablename__ = "states"

    id = Column(Integer(11), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
