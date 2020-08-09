#!/usr/bin/python3
"""
Lists all cities from the database
"""
if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)()
    cities = session.query(State).order_by(State.id)
    for stt in cities:
        for ct in stt.cities:
            print("{}: {} -> {}".format(ct.id, ct.name, stt.name))
