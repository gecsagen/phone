"""The module contains methods for working with a database"""

import redis
from schemas import FullDate, Phone, Address


class PersonalInfo:
    """Class for working with data at the database level"""

    def __init__(self):
        self.db_session = redis.Redis()

    # Creating a record with personal information
    async def create_personal_info(self, data: FullDate) -> None:
        self.db_session.mset({data.number: data.address})

    # Receiving a record with personal information
    async def get_personal_info(self, phone: Phone) -> Address:
        address = self.db_session.get(phone)
        return Address(full_address=address)

    # update a record with personal information
    async def update_personal_info(self, data: FullDate) -> None:
        self.db_session.hmset(data.number, data.model_dump(exclude_unset=True))
