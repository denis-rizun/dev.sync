from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.entities.session import SessionEntity


class ISessionService(ABC):

    @abstractmethod
    async def deactivate(self, ids: list[UUID]) -> None:
        pass

    @abstractmethod
    async def get_active_sessions(self) -> list[SessionEntity]:
        pass
