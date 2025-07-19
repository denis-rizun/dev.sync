from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.entities.user import UserEntity


class IUserService(ABC):

    @abstractmethod
    async def get_account(self, id: UUID) -> UserEntity:
        pass
