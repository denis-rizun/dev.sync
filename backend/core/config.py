from pathlib import Path
from uuid import UUID

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DevSyncConfig(BaseSettings):
    PROJECT_NAME: str = "dev.sync"
    VERSION: str = "0.1.0"
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    ENABLE_LOGGER: bool = True
    ENABLE_COLORED_LOGS: bool = True

    API_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    INNER_POSTGRES_PORT: int
    OUTER_POSTGRES_PORT: int
    POSTGRES_URL: str

    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    CELERY_BROKER_URL: str
    CELERY_BACKEND_URL: str
    CELERY_TASK_TRACK_STARTED: bool
    CELERY_TASK_TIME_LIMIT: int
    CELERY_TASK_SOFT_TIME_LIMIT: int
    CELERY_TIMEZONE: str
    CELERY_ENABLE_UTC: bool

    INNER_REDIS_PORT: int
    OUTER_REDIS_PORT: int

    CELERY_AUTH_TOKEN: UUID
    CELERY_AUTH_USER_ID: UUID

    @property
    def database_connection(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.INNER_POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    @property
    def public_key(self) -> str:
        with open(BASE_DIR / "public.pem") as file:
            return file.read()

    @property
    def private_key(self) -> str:
        with open(BASE_DIR / "private.pem") as file:
            return file.read()

    class Config:
        env_file = BASE_DIR / ".env"


config = DevSyncConfig()
