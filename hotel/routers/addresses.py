from fastapi import APIRouter
from hotel.operations.models import AddressResult
from hotel.operations.addresses import read_all_addresses, read_address

router = APIRouter()


@router.get("/addresses")
def api_read_all_addresses() -> list[AddressResult]:
    return read_all_addresses()


@router.get("/address/{address_id}")
def api_read_address(address_id: int) -> AddressResult:
    return read_address(address_id)
