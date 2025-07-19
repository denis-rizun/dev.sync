from abc import ABC

from backend.domain.abstractions.repositories import IRepository
from backend.domain.types import ModelType, EntityType, MapperType


class ISessionRepository(IRepository[ModelType, EntityType, MapperType], ABC):
    pass
