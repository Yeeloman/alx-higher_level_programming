#!/usr/bin/python3
"""Contains State class and Base"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata)


class State(Base):
    """
    Class that defines state
    table: the name of the table.
    id: the id
    name: the name:with expression as target:
        pass
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
