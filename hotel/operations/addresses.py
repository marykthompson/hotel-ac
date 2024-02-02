from hotel.db.engine import DBSession
from hotel.db.models import DBAddress, to_dict
from hotel.operations.models import AddressResult


def read_all_addresses() -> list[AddressResult]:
    session = DBSession()
    addresses: list[DBAddress] = session.query(DBAddress).all()
    print('addresses', addresses)
    result = [AddressResult(**to_dict(r)) for r in addresses]
    session.close()
    return result


def read_address(room_id: int) -> AddressResult:
    session = DBSession()
    room: DBAddress = session.query(DBAddress).get(room_id)
    result = AddressResult(**to_dict(room))
    session.close()
    return result
