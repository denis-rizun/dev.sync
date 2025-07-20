from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.dtos.history import HistoryUpdateDTO
from backend.domain.entities.history import HistoryEntity


class IHistoryService(ABC):

    @abstractmethod
    async def update(self, id: UUID, user_id: UUID, data: HistoryUpdateDTO) -> HistoryEntity:
        pass
