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
    states = session.query(State, City).filter(
        State.id == City.state_id).order_by(State.id, City.id)
    prev = 0
    for stt, ct in states:
        if prev == 0 or stt != prev:
            prev = stt
            flag = 1
        if flag == 1:
            print("{}: {}".format(stt.id, stt.name))
            print("\t{}: {}".format(ct.id, ct.name))
            flag = 0
        elif flag == 0:
            print("\t{}: {}".format(ct.id, ct.name))
