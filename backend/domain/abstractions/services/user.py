from abc import ABC, abstractmethod

from backend.domain.entities.user import UserEntity


class IUserService(ABC):

    @abstractmethod
    async def get_account(self, id: int) -> UserEntity:
        pass
