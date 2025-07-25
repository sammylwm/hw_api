from sqlalchemy import create_engine
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    db_url: str = "postgresql+asyncpg://sammy:Leto2025@pg:5432/hwApp"


settings = Setting()
