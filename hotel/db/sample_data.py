from hotel.db.models import DBCustomer, DBRoom, DBBooking, DBAddress
from datetime import date

addresses = [
    DBAddress(
        number=62,
        street_name="Sunny Rd",
        zipcode=12345,
        country="UK",
    ),
    DBAddress(number=46, street_name="Rainy Ln", zipcode=67890, country="UK"),
]

customers = [
    DBCustomer(
        first_name="John",
        last_name="Smith",
        email_address="email@email.com",
        marketing_emails=False,
        address_id=1,
    ),
    DBCustomer(
        first_name="Jane",
        last_name="Doe",
        email_address="jane@hotmail.com",
        marketing_emails=True,
        address_id=1,
    ),
    DBCustomer(
        first_name="Jack",
        last_name="Black",
        email_address="jack@black.com",
        marketing_emails=True,
        address_id=1,
    ),
    DBCustomer(
        first_name="Jill",
        last_name="White",
        email_address="jill@gmail.com",
        marketing_emails=True,
        address_id=2,
    ),
    DBCustomer(
        first_name="Arjan",
        last_name="Codes",
        email_address="hi@arjancodes.com",
        marketing_emails=False,
        address_id=2,
    ),
]

rooms = [
    DBRoom(number="101", size=10, price=150_00),
    DBRoom(number="102", size=10, price=150_00),
    DBRoom(number="103", size=20, price=250_00),
    DBRoom(number="104", size=20, price=250_00),
    DBRoom(number="105", size=30, price=350_00),
]

bookings = [
    DBBooking(
        from_date=date(2024, 1, 20),
        to_date=date(2024, 1, 30),
        price=250_00,
        cancellable=False,
        customer_id=1,
        room_id=1,
    )
]
