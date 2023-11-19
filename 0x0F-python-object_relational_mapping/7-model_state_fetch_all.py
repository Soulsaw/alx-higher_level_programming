#!/usr/bin/python3
"""The SQL definition of the base class
"""
import sys
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
Base = declarative_base()


class State(Base):
    """This class map the State tables
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(State).all()
for _row in query:
    print('{}: {}'.format(_row.id, _row.name))
