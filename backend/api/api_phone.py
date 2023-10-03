"""The module contains an API for processing web requests from users"""

from fastapi import APIRouter

phone_router = APIRouter()


@phone_router.get("/check_data")
async def root():
    return {"message": "Hello World"}
