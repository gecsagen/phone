"""The module contains methods for working with a database"""

import redis
from schemas import FullDate, Phone, Address

r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

print(r.get("Bahamas"))

from typing import Union
from uuid import UUID


class PersonalInfo:
    """Class for working with data at the database level"""

    def __init__(self):
        self.db_session = redis.Redis()

    # Creating a record with personal information
    async def create_personal_info(self, data: FullDate) -> None:
        self.db_session.mset({"phone":[data.number, data.address]})

    # Receiving a record with personal information
    async def get_personal_info(phone: Phone) -> Address:
        self.db_session
        
