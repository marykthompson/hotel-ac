from sqlalchemy import Column, Date, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def to_dict(obj: Base):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


class DBAddress(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    street_name = Column(String(250), nullable=False)
    zipcode = Column(Integer, nullable=False)
    country = Column(String(250), nullable=False)


class DBAmenity(Base):
    __tablename__ = "amenity"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # note that for the foreign key we use the table name, not the class name
    owner = Column(Integer, ForeignKey("customer.id"))


class DBCustomer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    marketing_emails = Column(Boolean, nullable=False)

    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship(DBAddress)


class DBRoom(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class DBBooking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    cancellable = Column(Boolean, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship(DBCustomer)
    room_id = Column(Integer, ForeignKey("room.id"))
    room = relationship(DBRoom)
