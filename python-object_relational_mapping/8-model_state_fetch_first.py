#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Database connection
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state by id
    first_state = session.query(State).order_by(State.id).first()

    # Display result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
