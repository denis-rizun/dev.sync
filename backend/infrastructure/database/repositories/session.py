from typing import Any

from sqlalchemy import select, update

from backend.domain.abstractions.repositories.session import ISessionRepository
from backend.domain.entities.session import SessionEntity
from backend.domain.enums.common import ColumnEnum
from backend.infrastructure.database.models import SessionModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.session import SessionMapper


class SessionRepository(
    BaseRepository[SessionModel, SessionEntity, SessionMapper],
    ISessionRepository[SessionModel, SessionEntity, SessionMapper]
):
    MODEL = SessionModel
    MAPPER = SessionMapper

    async def get_active_session(self, user_id: int, token: str) -> SessionEntity | None:
        stmt = (
            select(self.MODEL)
            .where(self.MODEL.user_id == user_id)
            .where(self.MODEL.revoked == False)  # noqa: E712
            .where(self.MODEL.refresh_token == token)
        )
        result = await self.session.execute(stmt)
        found = result.scalar_one_or_none()
        return self.MAPPER.to_entity(found) if found else None

    async def update_many(
            self,
            column: ColumnEnum,
            values: list[Any],
            data: dict[ColumnEnum, Any]
    ) -> None:
        stmt = (
            update(self.MODEL)
            .where(getattr(self.MODEL, column.value).in_(values))
            .values({col.value: val for col, val in data.items()})
        )
        await self.session.execute(stmt)
