from abc import ABC

from backend.domain.abstractions.repositories import IRepository
from backend.domain.types import MapperType, EntityType, ModelType


class IServerRepository(IRepository[ModelType, EntityType, MapperType], ABC):
    pass
