from abc import ABC, abstractmethod

from backend.domain.abstractions.repositories import IRepository
from backend.domain.types import ModelType, EntityType, MapperType


class ISessionRepository(IRepository[ModelType, EntityType, MapperType], ABC):

    @abstractmethod
    async def get_active_session(self, user_id: int, token: str) -> EntityType | None:
        pass
