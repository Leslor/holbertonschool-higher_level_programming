#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class City(Base):
    """class definition of a City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement='auto',
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    relationship('State')
