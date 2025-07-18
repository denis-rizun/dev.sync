from abc import ABC, abstractmethod
from typing import Any, Generic, Type

from backend.domain.enums.common import ColumnEnum
from backend.domain.enums.repository import OrderByEnum
from backend.domain.types import ModelType, EntityType, MapperType


class IRepository(ABC, Generic[ModelType, EntityType, MapperType]):
    MODEL: Type[ModelType]
    MAPPER: Type[MapperType]

    @abstractmethod
    async def create(self, entity: EntityType) -> ModelType:
        pass

    @abstractmethod
    async def get(
            self,
            column: ColumnEnum,
            value: Any,
            is_many: bool = False
    ) -> ModelType | list[ModelType] | None:
        pass

    @abstractmethod
    async def get_filtered(
            self,
            filters: dict[ColumnEnum, Any],
            is_many: bool = False,
            unique: bool = False,
            order_by: OrderByEnum | None = None,
            limit: int | None = None,
            offset: int | None = None,
            options: list[Any] | None = None
    ) -> ModelType | list[ModelType] | None:
        pass

    @abstractmethod
    async def get_existed(self, column: ColumnEnum, value: Any) -> ModelType:
        pass

    @abstractmethod
    async def update(self, column: ColumnEnum, value: Any, data: dict[ColumnEnum, Any]) -> ModelType:
        pass

    @abstractmethod
    async def delete(self, column: ColumnEnum, value: Any) -> None:
        pass
