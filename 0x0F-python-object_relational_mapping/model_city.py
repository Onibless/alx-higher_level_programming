#!/usr/bin/python3
"""  python file that contains the
class definition of a City and an instance
Base = declarative_base(): """

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """definition of a City and an instance

    Args:
        Base (class): sqlalchemy convention
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
