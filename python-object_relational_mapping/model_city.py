#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """
    City class that represents the cities table in the database.
    
    Attributes:
        id (int): Auto-generated, unique identifier for each city.
        name (str): Name of the city (max length 128, not null).
        state_id (int): Foreign key referencing the id of the
        state in states table.
    """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
