from abc import ABC, abstractmethod
from typing import Any, Generic

from backend.domain.enums.common import ColumnEnum
from backend.domain.types import ModelType, EntityType, MapperType


class IRepository(ABC, Generic[ModelType, EntityType, MapperType]):
    MODEL: type[ModelType]
    MAPPER: type[MapperType]

    @abstractmethod
    async def create(self, entity: EntityType) -> EntityType:
        pass

    @abstractmethod
    async def get(
            self,
            column: ColumnEnum,
            value: Any,
            is_many: bool = False
    ) -> EntityType | list[EntityType] | None:
        pass

    @abstractmethod
    async def get_existed(self, column: ColumnEnum, value: Any) -> EntityType:
        pass

    @abstractmethod
    async def update(
            self,
            column: ColumnEnum,
            value: Any,
            data: dict[ColumnEnum, Any]
    ) -> EntityType:
        pass

    @abstractmethod
    async def delete(self, column: ColumnEnum, value: Any) -> None:
        pass
