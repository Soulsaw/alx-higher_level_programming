#!/usr/bin/python3
"""The SQL definition of the base class
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(State).all()
for _row in query:
    print('{}: {}'.format(_row.id, _row.name))
