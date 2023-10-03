"""The module contains service functions"""
from .schemas import Phone, Address, FullDate


#  service for obtaining an address
async def _check_data(phone: Phone) -> Address:
    return {"message": phone}


#  service for adding phone number and address
async def _write_data(phone_address: FullDate):
    return {"message": FullDate(number="test", address="test")}


#  service for updating phone number and address
async def _update_data(phone_address: FullDate):
    return {"message": FullDate(number="test", address="test")}
