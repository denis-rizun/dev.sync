from typing import Any

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.domain.abstractions.repositories import IRepository
from backend.domain.enums.common import ColumnEnum
from backend.domain.enums.repository import OrderByEnum
from backend.domain.types import ModelType, EntityType, MapperType


class BaseRepository(IRepository[ModelType, EntityType, MapperType]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, entity: EntityType) -> EntityType:
        model = self.MAPPER.to_model(entity)
        self.session.add(model)
        await self.session.flush()
        return self.MAPPER.to_entity(model)

    async def get(
            self,
            column: ColumnEnum,
            value: Any,
            is_many: bool = False
    ) -> EntityType | list[EntityType] | None:
        stmt = select(self.MODEL).where(getattr(self.MODEL, column.value) == value)
        result = await self.session.execute(stmt)
        found = result.scalars().all() if is_many else result.scalar_one_or_none()

        if found:
            if isinstance(found, list):
                return [self.MAPPER.to_entity(model) for model in found]

            return self.MAPPER.to_entity(found)
        return None

    async def get_existed(self, column: ColumnEnum, value: Any) -> EntityType:
        stmt = select(self.MODEL).where(getattr(self.MODEL, column.value) == value)
        result = await self.session.execute(stmt)
        found = result.scalar_one()
        return self.MAPPER.to_entity(found)

    async def get_filtered(
            self,
            filters: dict[ColumnEnum, Any],
            is_many: bool = False,
            unique: bool = False,
            order_by: OrderByEnum | None = None,
            limit: int | None = None,
            offset: int | None = None,
            options: list[Any] | None = None
    ) -> EntityType | list[EntityType] | None:
        stmt = select(self.MODEL)
        if options:
            for opt in options:
                stmt = stmt.options(opt)

        for field, value in filters.items():
            column = getattr(self.MODEL, field.value)

            if isinstance(value, (list, tuple, set)):
                stmt = stmt.where(column.in_(value))
            else:
                stmt = stmt.where(column == value)

        if order_by:
            stmt = stmt.order_by(getattr(self.MODEL, order_by))

        if limit is not None:  # limit=0 -> python interprets like False
            stmt = stmt.limit(limit)

        if offset is not None:  # offset=0 -> python interprets like False
            stmt = stmt.offset(offset)

        result = await self.session.execute(stmt)
        scalars = result.unique().scalars() if unique else result.scalars()
        found = scalars.all() if is_many else scalars.first()

        if found:
            if isinstance(found, list):
                return [self.MAPPER.to_entity(model) for model in found]

            return self.MAPPER.to_entity(found)
        return None

    async def update(
            self,
            column: ColumnEnum,
            value: Any,
            data: dict[ColumnEnum, Any]
    ) -> EntityType:
        stmt = (
            update(self.MODEL)
            .where(getattr(self.MODEL, column.value) == value)
            .values(**{key.value: val for key, val in data.items()})
            .returning(self.MODEL)
        )
        result = await self.session.execute(stmt)
        await self.session.flush()
        model = result.scalar_one()
        return self.MAPPER.to_entity(model)

    async def delete(self, column: ColumnEnum, value: Any) -> None:
        stmt = delete(self.MODEL).where(getattr(self.MODEL, column.value) == value)
        await self.session.execute(stmt)
