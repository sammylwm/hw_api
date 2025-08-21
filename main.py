from fastapi.middleware.cors import CORSMiddleware
from api_v1 import router as routers_api
from config_reader import app, config
# from bot.handlers import setup_routers

import uvicorn

from core.models import db_helper

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# dp.include_router(setup_routers())

app.include_router(routers_api)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config.APP_HOST,
        port=config.APP_PORT,
    )
