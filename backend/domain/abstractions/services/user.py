from abc import ABC, abstractmethod

from backend.domain.dtos.user import RegistrationDTO, LoginDTO
from backend.domain.entities.user import UserEntity


class IUserService(ABC):

    @abstractmethod
    async def registrate(self, data: RegistrationDTO) -> UserEntity:
        pass

    @abstractmethod
    async def login(self, data: LoginDTO) -> UserEntity:
        pass

    @abstractmethod
    async def logout(self) -> None:
        pass
