from uuid import UUID

from backend.core.exceptions import NotFoundError, PermissionDeniedError
from backend.core.logger import Logger
from backend.domain.abstractions.repositories.history import IHistoryRepository
from backend.domain.abstractions.services.history import IHistoryService
from backend.domain.dtos.history import HistoryUpdateDTO
from backend.domain.entities.history import HistoryEntity
from backend.domain.enums.common import ColumnEnum

logger = Logger.setup_logger(__name__)


class HistoryService(IHistoryService):
    def __init__(self, history_repo: IHistoryRepository) -> None:
        self._history_repo = history_repo

    async def update(self, id: UUID, user_id: UUID, data: HistoryUpdateDTO) -> HistoryEntity:
        existing = await self._history_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='History not found')

        updated_history = await self._history_repo.update(
            column=ColumnEnum.ID,
            value=id,
            data=data.to_raw()
        )
        logger.info(f"[HistoryService]: Updated history: {updated_history!r}")
        return updated_history
