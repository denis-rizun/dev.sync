from abc import ABC, abstractmethod

from backend.domain.abstractions.repositories import IRepository
from backend.domain.types import ModelType, EntityType, MapperType


class IUserRepository(IRepository[ModelType, EntityType, MapperType], ABC):

    @abstractmethod
    async def get_by_username_or_mail(self, username: str, mail: str) -> EntityType | None:
        pass
