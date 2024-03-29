import logging
import uvicorn
from fastapi import FastAPI

from api.api_phone import phone_router


log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI(debug=True)
    application.include_router(phone_router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
