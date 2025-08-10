from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = "postgresql+asyncpg://sammy:Leto2025@hwApp_pg:5432/hwApp"
    db_echo: bool = False



settings = Setting()
