from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from backend.core.config import config


class DatabaseInitializer:
    @classmethod
    def initialize(cls, echo: bool = False, expire: bool = False) -> async_sessionmaker:
        engine = cls._create_engine(echo=echo)
        return cls._create_session_pool(engine=engine, expire=expire)

    @classmethod
    def _create_engine(cls, echo: bool) -> AsyncEngine:
        return create_async_engine(
            url=config.database_connection,
            query_cache_size=1200,
            pool_size=20,
            max_overflow=200,
            future=True,
            echo=echo,
        )

    @classmethod
    def _create_session_pool(cls, engine: AsyncEngine, expire: bool) -> async_sessionmaker:
        return async_sessionmaker(bind=engine, expire_on_commit=expire)



