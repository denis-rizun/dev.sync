from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.dtos.server import ServerCreateDTO, ServerUpdateDTO
from backend.domain.entities.server import ServerEntity


class IServerService(ABC):

    @abstractmethod
    async def get_servers_info(self, user_id: UUID) -> list[ServerEntity | None]:
        pass

    @abstractmethod
    async def create(self, data: ServerCreateDTO, user_id: UUID) -> ServerEntity:
        pass

    @abstractmethod
    async def update(self, id: UUID, user_id: UUID, data: ServerUpdateDTO) -> ServerEntity:
        pass

    @abstractmethod
    async def delete(self, id: UUID, user_id: UUID) -> None:
        pass
