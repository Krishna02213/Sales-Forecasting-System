from pydantic_settings import BaseSettings
from typing import List
import os


IS_VERCEL = bool(os.getenv("VERCEL"))
DEFAULT_DATABASE_URL = (
    "sqlite+aiosqlite:////tmp/sales_forecast.db"
    if IS_VERCEL
    else "sqlite+aiosqlite:///./sales_forecast.db"
)
DEFAULT_UPLOAD_DIR = "/tmp/uploads" if IS_VERCEL else "./uploads"
DEFAULT_MODELS_DIR = "/tmp/trained_models" if IS_VERCEL else "./trained_models"


class Settings(BaseSettings):
    DATABASE_URL: str = DEFAULT_DATABASE_URL
    SECRET_KEY: str = "changeme-super-secret-key-32chars"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    REDIS_URL: str = "redis://localhost:6379/0"
    UPLOAD_DIR: str = DEFAULT_UPLOAD_DIR
    MODELS_DIR: str = DEFAULT_MODELS_DIR
    MAX_UPLOAD_SIZE: int = 52428800
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://localhost:80"]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.MODELS_DIR, exist_ok=True)
