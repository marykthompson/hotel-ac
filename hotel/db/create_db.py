from hotel.db.models import Base
from hotel.db.sample_data import customers, rooms, bookings, addresses
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db(file: str):
    engine = create_engine(file)
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Insert a few customers into the customers table
    session.add_all(customers)

    # Insert a few rooms into the rooms table
    session.add_all(rooms)

    # Insert a few bookings into the bookings table
    session.add_all(bookings)

    # Insert addresses into the addresses table
    session.add_all(addresses)

    session.commit()
