from abc import ABC, abstractmethod

from backend.domain.dtos.history import HistoryCreateDTO
from backend.domain.entities.history import HistoryEntity


class IHistoryService(ABC):

    @abstractmethod
    async def create(self, data: HistoryCreateDTO) -> HistoryEntity:
        pass
