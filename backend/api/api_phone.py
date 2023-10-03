"""The module contains an API for processing web requests from users"""

from fastapi import APIRouter
from .schemas import Phone, Address, FullDate

phone_router = APIRouter()


#  endpoint for getting phone and address
@phone_router.get("/check_data")
async def check_data(phone: Phone) -> Address:
    return {"message": "Hello World"}


#  endpoint for creating phone and address
@phone_router.post("/write_data")
async def write_data(data: FullDate):
    return {"message": "Hello World"}


#  endpoint for updating phone and address
@phone_router.put("/write_data")
async def update_data(data: FullDate):
    return {"message": "Hello World"}
