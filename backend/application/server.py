from uuid import UUID

from backend.core.exceptions import NotFoundError, PermissionDeniedError, ConflictError
from backend.core.logger import Logger
from backend.core.utils import Mapper
from backend.domain.abstractions.repositories.server import IServerRepository
from backend.domain.abstractions.services.server import IServerService
from backend.domain.dtos.server import ServerCreateDTO
from backend.domain.entities.server import ServerEntity
from backend.domain.enums.common import ColumnEnum, ServerStatusEnum

logger = Logger.setup_logger(__name__)


class ServerService(IServerService):
    def __init__(self, server_repo: IServerRepository) -> None:
        self._server_repo = server_repo

    async def get_servers_info(self, user_id: UUID) -> list[ServerEntity | None]:
        servers = await self._server_repo.get(
            column=ColumnEnum.USER_ID,
            value=user_id,
            is_many=True
        )
        return servers if isinstance(servers, list) else []

    async def create(self, data: ServerCreateDTO, user_id: UUID) -> ServerEntity:
        entity = Mapper.to_entity(entity=ServerEntity, dto=data)
        entity.user_id = user_id

        new_server = await self._server_repo.create(entity=entity)
        logger.info(f"[ServerService]: Created server: {new_server!r}")
        return new_server

    async def deactivate(self, id: UUID, user_id: UUID) -> ServerEntity:
        existing = await self._server_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Server not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        if existing.server_status == ServerStatusEnum.INACTIVE:
            raise ConflictError(message='Server already inactive')

        updated_server = await self._server_repo.update(
            column=ColumnEnum.ID,
            value=existing.id,
            data={ColumnEnum.SERVER_STATUS: ServerStatusEnum.INACTIVE}
        )
        logger.info(f"[ServerService]: Deactivated server: {updated_server!r}")
        return updated_server

    async def delete(self, id: UUID, user_id: UUID) -> None:
        existing = await self._server_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Server not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        await self._server_repo.delete(column=ColumnEnum.ID, value=id)
        logger.info(f"[ServerService]: Deleted server: {id}")
