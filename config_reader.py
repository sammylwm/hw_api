from contextlib import asynccontextmanager
from typing import AsyncGenerator
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram import Bot, Dispatcher
from fastapi import FastAPI


class Config(BaseSettings):
    BOT_TOKEN: SecretStr
    WEBHOOK_URL: str
    WEBAPP_URL: str
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = "8000"
    DB_URL: SecretStr

    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    await bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/webhook",
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True,
    )
    yield
    await bot.session.close()


config = Config()
bot = Bot(
    config.BOT_TOKEN.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()
app = FastAPI(lifespan=lifespan)
