from pathlib import Path
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

# BASE_DIR = Path(__file__).parent.parent.parent
# DB_PATH = BASE_DIR / "db.sqlite3"
load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# f"sqlite+aiosqlite:///{DB_PATH}"
class DbSettings(BaseModel):
    url: str = f"{DB_URL}"
    echo: bool = False


class Settings(BaseSettings):
    db: DbSettings = DbSettings()
    # db_echo: bool = False
    # api_v1_prefix: str = "/api/v1"
    db_echo: bool = True


settings = Settings()
