#!/usr/bin/python3

"""script that creates the State “California”
with the City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """state class object
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
