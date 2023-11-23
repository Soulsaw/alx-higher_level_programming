#!/usr/bin/python3
"""The SQL definition of the base class
"""
import sys
from relationship_city import City
from relationship_state import State
from relationship_state import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    session.add(state)
    session.commit()
    city = City(name="San Francisco", state_id=state.id)
    session.add(city)
    session.commit()
