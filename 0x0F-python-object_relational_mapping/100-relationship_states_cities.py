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
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    cali = State(name='California')
    sf = City(name='San Francisco')
    cali.cities = [sf]
    session.add(cali)
    session.commit()
