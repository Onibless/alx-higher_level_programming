#!/usr/bin/python3
"""Improve the files model_city.py and
model_state.py, and save them as
relationship_city.py and relationship_state.py:
City class:
No change
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    Same city class without change
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
