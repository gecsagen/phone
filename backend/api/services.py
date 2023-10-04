"""The module contains service functions"""
from .schemas import Phone, Address, FullDate
from dals import PersonalInfo


#  service for obtaining an address
async def _check_data(phone: Phone) -> Address:
    personal_dal = PersonalInfo()
    personal_date = await personal_dal.get_personal_info(phone=phone)
    return personal_date


#  service for adding phone number and address
async def _write_data(full_date: FullDate):
    personal_dal = PersonalInfo()
    await personal_dal.create_personal_info(data=full_date)


#  service for updating phone number and address
async def _update_data(full_date: FullDate):
    personal_dal = PersonalInfo()
    await personal_dal.update_personal_info(data=full_date)
