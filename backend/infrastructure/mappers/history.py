from backend.domain.entities.history import HistoryEntity
from backend.infrastructure.database.models import HistoryModel
from backend.infrastructure.mappers.base import BaseMapper


class HistoryMapper(BaseMapper[HistoryEntity, HistoryModel]):
    ENTITY = HistoryEntity
    MODEL = HistoryModel
