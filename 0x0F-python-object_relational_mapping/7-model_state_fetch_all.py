#!/usr/bin/python3
"""
Lists all cities from the database
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    states = session.query(State).order_by(State.id.asc()).all()
    for stt in states:
        print("{}: {}".format(stt.id, stt.name))
