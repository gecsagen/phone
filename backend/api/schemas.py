"""the module contains the necessary pydantic models"""


from pydantic import BaseModel
from pydantic.types import ph


class Phone(BaseModel):
    """Phone number model"""

    number: str


class Address(BaseModel):
    """Address model"""

    full_address: str


class FullDate(BaseModel):
    number: Phone
    address: Address
