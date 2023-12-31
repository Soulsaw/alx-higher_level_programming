#!/usr/bin/python3
"""The SQL definition of the base class
"""
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    _row = session.query(State.id).filter_by(name=sys.argv[4]).first()
    if _row is None:
        print('Not found')
    else:
        print(_row[0])
