from hotel.db.engine import DBSession
from hotel.db.models import DBBooking, DBRoom, to_dict
from hotel.operations.models import BookingCreateData, BookingResult


def read_all_bookings() -> list[BookingResult]:
    session = DBSession()
    bookings: list[DBBooking] = session.query(DBBooking).all()
    result = [BookingResult(**to_dict(b)) for b in bookings]
    session.close()
    return result


def read_booking(booking_id: int) -> BookingResult:
    session = DBSession()
    booking: DBBooking = session.query(DBBooking).get(booking_id)
    result = BookingResult(**to_dict(booking))
    session.close()
    return result


def create_booking(data: BookingCreateData) -> BookingResult:
    session = DBSession()

    # retrieve the room
    room = session.query(DBRoom).get(data.room_id)

    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise ValueError("Invalid dates")

    booking = DBBooking(**data.dict())
    booking.price = room.price * days
    session.add(booking)
    session.commit()
    result = BookingResult(**to_dict(booking))
    session.close()
    return result


def delete_booking(booking_id: int) -> BookingResult:
    session = DBSession()
    booking: DBBooking = session.query(DBBooking).get(booking_id)
    result = BookingResult(**to_dict(booking))
    session.delete(booking)
    session.commit()
    session.close()
    return result
