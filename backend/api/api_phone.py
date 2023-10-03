"""The module contains an API for processing web requests from users"""

from fastapi import APIRouter

phone_router = APIRouter()


#  endpoint for getting phone and address
@phone_router.get("/check_data")
async def check_data():
    return {"message": "Hello World"}


#  endpoint for creating phone and address
@phone_router.post("/write_data")
async def write_data():
    return {"message": "Hello World"}


#  endpoint for updating phone and address
@phone_router.put("/write_data")
async def update_data():
    return {"message": "Hello World"}
