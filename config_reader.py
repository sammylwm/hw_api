from pydantic_settings import BaseSettings
from fastapi import FastAPI


class Config(BaseSettings):
    WEBHOOK_URL: str = "https://lednevs.ru/hw_api/api"
    WEBAPP_URL: str = "https://lednevs.ru/hw_api"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = "8000"
    DB_URL: str = "postgresql+asyncpg://sammy:Dosya1009@db:5432/hwApp"


config = Config()
app = FastAPI()
