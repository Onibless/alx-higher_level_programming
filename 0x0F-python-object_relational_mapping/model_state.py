#!/usr/bin/python3
"""  python file that contains the
class definition of a State and an instance
Base = declarative_base(): """

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """definition of a State and an instance

    Args:
        Base (class): sqlalchemy convention
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
