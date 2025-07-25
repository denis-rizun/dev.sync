from abc import ABC, abstractmethod
from typing import Any

from backend.domain.abstractions.repositories import IRepository
from backend.domain.enums.common import ColumnEnum
from backend.domain.types import ModelType, EntityType, MapperType


class ISessionRepository(IRepository[ModelType, EntityType, MapperType], ABC):

    @abstractmethod
    async def get_active_session(self, user_id: int, token: str) -> EntityType | None:
        pass

    @abstractmethod
    async def update_many(
            self,
            column: ColumnEnum,
            values: list[Any],
            data: dict[ColumnEnum, Any]
    ) -> None:
        pass
