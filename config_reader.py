from contextlib import asynccontextmanager
from typing import AsyncGenerator
from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram import Bot, Dispatcher
from fastapi import FastAPI


class Config(BaseSettings):
    WEBHOOK_URL: str = "https://lednevs.ru/hw_api/api"
    WEBAPP_URL: str = "https://lednevs.ru/hw_api"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = "8000"
    DB_URL: str = "postgresql+asyncpg://sammy:Dosya1009@db:5432/hwApp"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    # await bot.set_webhook(
    #     url=f"{config.WEBHOOK_URL}/webhook",
    #     allowed_updates=dp.resolve_used_update_types(),
    #     drop_pending_updates=True,
    # )
    yield
    # await bot.session.close()


config = Config()
# bot = Bot(
#     config.BOT_TOKEN.get_secret_value(),
#     default=DefaultBotProperties(parse_mode=ParseMode.HTML),
# )
# dp = Dispatcher()
app = FastAPI(lifespan=lifespan)
