#!/usr/bin/python3
"""The SQL definition of the base class
"""
import sys
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for instance in session.query(State).order_by(State.id).all():
        for city_ins in instance.cities:
            print(city_ins.id, city_ins.name, sep=': ', end='')
            print(' -> ' + instance.name)
