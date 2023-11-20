#!/usr/bin/python3
"""The SQL definition of the base class
"""
import sys
from model_city import City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).order_by(City.id)
    for c, s in query.filter(City.state_id == State.id).all():
        print(s.name, '({}) {}'.format(c.id, c.name), sep=": ")
