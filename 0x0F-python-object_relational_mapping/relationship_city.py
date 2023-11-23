#!/usr/bin/python3
"""The SQL definition of the base class
"""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, String, Integer


class City(Base):
    """This class map the State tables
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
