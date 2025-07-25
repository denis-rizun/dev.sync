from backend.core.logger import Logger
from backend.core.utils import Mapper
from backend.domain.abstractions.repositories.history import IHistoryRepository
from backend.domain.abstractions.services.history import IHistoryService
from backend.domain.dtos.history import HistoryCreateDTO
from backend.domain.entities.history import HistoryEntity

logger = Logger.setup_logger(__name__)


class HistoryService(IHistoryService):
    def __init__(self, history_repo: IHistoryRepository) -> None:
        self._history_repo = history_repo

    async def create(self, data: HistoryCreateDTO) -> HistoryEntity:
        entity = Mapper.to_entity(entity=HistoryEntity, dto=data)
        new_history = await self._history_repo.create(entity=entity)
        logger.info(f"[HistoryService]: Created history: {new_history!r}")
        return new_history
