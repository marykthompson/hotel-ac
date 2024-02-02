from hotel.db.engine import DBSession
from hotel.db.models import DBRoom, to_dict
from hotel.operations.models import RoomResult


def read_all_rooms() -> list[RoomResult]:
    session = DBSession()
    rooms: list[DBRoom] = session.query(DBRoom).all()
    result = [RoomResult(**to_dict(r)) for r in rooms]
    session.close()
    return result


def read_room(room_id: int) -> RoomResult:
    session = DBSession()
    room: DBRoom = session.query(DBRoom).get(room_id)
    result = RoomResult(**to_dict(room))
    session.close()
    return result
