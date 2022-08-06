#!/usr/bin/python3
'''This Script lists all states from the database
hbtn_0e_0_usa'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """class definition of a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement='auto',
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
