#!/usr/bin/python3
"""contains the class definition of a City."""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey

mt_data = MetaData()
Base = declarative_base(metadata=mt_data)


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state_id"), nullable=False)
