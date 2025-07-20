from backend.domain.abstractions.repositories.history import IHistoryRepository
from backend.domain.entities.history import HistoryEntity
from backend.infrastructure.database.models import HistoryModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.history import HistoryMapper


class SessionRepository(
    BaseRepository[HistoryModel, HistoryEntity, HistoryMapper],
    IHistoryRepository[HistoryModel, HistoryEntity, HistoryMapper]
):
    MODEL = HistoryModel
    MAPPER = HistoryMapper
