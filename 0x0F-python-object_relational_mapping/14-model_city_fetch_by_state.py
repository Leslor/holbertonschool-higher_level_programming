#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    """script 14-model_city_fetch_by_state.py that prints all
    City objects"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        for city, state in session.query(City, State).filter_by(
                state_id=State.id).order_by(City.id).all():
            print(f'{state.name}: ({city.id}) {city.name}')
