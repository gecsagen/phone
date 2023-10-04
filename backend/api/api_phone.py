"""The module contains an API for processing web requests from users"""
from logging import getLogger
from fastapi import APIRouter
from .schemas import Phone, Address, FullDate
from fastapi import HTTPException
from .services import _write_data, _check_data, _update_data


logger = getLogger(__name__)

phone_router = APIRouter()


#  endpoint for getting phone and address
@phone_router.get("/check_data")
async def check_data(phone: str) -> Address:
    personal_date = await _check_data(phone)
    if personal_date is None:
        raise HTTPException(status_code=404, detail=f"User with id {phone} not found.")
    return personal_date


#  endpoint for creating phone and address
@phone_router.post("/write_data")
async def write_data(data: FullDate):
    try:
        #  вызывается функция создания нового пользователя
        return await _write_data(data)
    except Exception as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")


#  endpoint for updating phone and address
@phone_router.put("/write_data")
async def update_data(data: FullDate):
    try:
        #  вызывается функция создания нового пользователя
        return await _update_data(data)
    except Exception as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")
