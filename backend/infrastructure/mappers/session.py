from backend.domain.entities.session import SessionEntity
from backend.infrastructure.database.models import SessionModel
from backend.infrastructure.mappers.base import BaseMapper


class SessionMapper(BaseMapper[SessionEntity, SessionModel]):
    ENTITY = SessionEntity
    MODEL = SessionModel
