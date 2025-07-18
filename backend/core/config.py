from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DevSyncConfig(BaseSettings):
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]

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
            f"{self.WEB_POSTGRES_USER}:{self.WEB_POSTGRES_PASSWORD}"
            f"@{self.WEB_POSTGRES_HOST}:{self.WEB_INNER_POSTGRES_PORT}"
            f"/{self.WEB_POSTGRES_DB}"
        )

    class Config:
        env_file = BASE_DIR / ".env"


config = DevSyncConfig()
