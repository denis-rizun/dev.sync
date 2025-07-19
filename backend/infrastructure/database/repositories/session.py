from datetime import datetime

from sqlalchemy import select

from backend.domain.abstractions.repositories.session import ISessionRepository
from backend.domain.entities.session import SessionEntity
from backend.infrastructure.database.models import SessionModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.session import SessionMapper


class SessionRepository(
    BaseRepository[SessionModel, SessionEntity, SessionMapper],
    ISessionRepository[SessionModel, SessionEntity, SessionMapper]
):
    MODEL = SessionModel
    MAPPER = SessionMapper

    async def get_active_session(self, user_id: int, token: str | None = None) -> SessionEntity | None:
        stmt = (
            select(self.MODEL)
            .where(self.MODEL.user_id == user_id)
            .where(self.MODEL.revoked == False)
            .where(self.MODEL.expired_at > datetime.now())
            .where(self.MODEL.refresh_token == token)
        )
        result = await self.session.execute(stmt)
        found = result.scalar_one_or_none()
        return self.MAPPER.to_entity(found) if found else None
