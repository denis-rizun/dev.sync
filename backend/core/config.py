from pathlib import Path

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

    @property
    def database_connection(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.INNER_POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = BASE_DIR / ".env"


config = DevSyncConfig()
