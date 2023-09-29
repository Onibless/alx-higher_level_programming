#!/usr/bin/python3
"""script that creates the State “California”
with the City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

from relationship_city import City
from relationship_state import Base, State
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    db = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
          'port': '3306', 'username': argv[1],
          'password': argv[2], 'database': argv[3]}

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    city = City(name='San Francisco')
    state = State(name='California', cities=[city])
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
