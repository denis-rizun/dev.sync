from abc import ABC, abstractmethod

from backend.domain.dtos.auth import RegistrationDTO, LoginDTO
from backend.domain.entities.token import TokenEntity
from backend.domain.entities.user import UserEntity


class IAuthService(ABC):

    @abstractmethod
    async def register(self, data: RegistrationDTO) -> UserEntity:
        pass

    @abstractmethod
    async def login(self, data: LoginDTO) -> UserEntity:
        pass

    @abstractmethod
    async def logout(self, id: int, token: str | None) -> None:
        pass

    @abstractmethod
    async def refresh_access_token(self, token: str | None) -> TokenEntity:
        pass
