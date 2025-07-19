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
