from abc import ABC, abstractmethod

from backend.domain.abstractions.repositories import IRepository
from backend.domain.types import ModelType, EntityType, MapperType


class IWebhookRepository(IRepository[ModelType, EntityType, MapperType], ABC):

    @abstractmethod
    async def get_with_server(self, key: str) -> EntityType | None:
        pass

