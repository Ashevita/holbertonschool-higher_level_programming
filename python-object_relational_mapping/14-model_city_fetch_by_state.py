#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get MySQL username, password, and database name from arguments
    user, pwd, db = argv[1], argv[2], argv[3]

    # Connect to MySQL database on localhost at port 3306
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query City objects, ordered by cities.id
    results = (session.query(State.name, City.id, City.name)
               .join(City).order_by(City.id).all())

    # Print results in the specified format
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close session
    session.close()
