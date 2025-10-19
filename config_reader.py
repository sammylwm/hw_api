from pydantic_settings import BaseSettings
from fastapi import FastAPI


class Config(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://sammy:Dosya1009@db:5432/hwApp"


config = Config()
app = FastAPI()
