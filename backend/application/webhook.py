from uuid import UUID

from backend.core.exceptions import NotFoundError, PermissionDeniedError, ConflictError
from backend.core.logger import Logger
from backend.core.utils import Mapper
from backend.domain.abstractions.repositories.history import IHistoryRepository
from backend.domain.abstractions.repositories.server import IServerRepository
from backend.domain.abstractions.repositories.webhook import IWebhookRepository
from backend.domain.abstractions.services.webhook import IWebhookService
from backend.domain.dtos.webhook import WebhookCreateDTO
from backend.domain.entities.history import HistoryEntity
from backend.domain.entities.webhook import WebhookEntity
from backend.domain.enums.common import ColumnEnum, ServerStatusEnum, StatusEnum
from backend.domain.enums.history import HistoryTriggerEnum

logger = Logger.setup_logger(__name__)


class WebhookService(IWebhookService):
    def __init__(
            self,
            webhook_repo: IWebhookRepository,
            server_repo: IServerRepository,
            history_repo: IHistoryRepository
    ) -> None:
        self._webhook_repo = webhook_repo
        self._server_repo = server_repo
        self._history_repo = history_repo

    async def get_webhooks(self, user_id: UUID) -> list[WebhookEntity | None]:
        webhooks = await self._webhook_repo.get(
            column=ColumnEnum.USER_ID,
            value=user_id,
            is_many=True
        )
        return webhooks if isinstance(webhooks, list) else []

    async def create(self, data: WebhookCreateDTO, user_id: UUID) -> WebhookEntity:
        entity = Mapper.to_entity(entity=WebhookEntity, dto=data)
        entity.user_id = user_id

        existing_server = await self._server_repo.get(column=ColumnEnum.ID, value=entity.server_id)
        if not existing_server:
            raise NotFoundError(message='Server not found')

        new_webhook = await self._webhook_repo.create(entity=entity)
        logger.info(f"[WebhookService]: Created webhook: {new_webhook!r}")
        return new_webhook

    async def deactivate(self, id: UUID, user_id: UUID) -> WebhookEntity:
        existing = await self._webhook_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        if existing.server_status == ServerStatusEnum.INACTIVE:
            raise ConflictError(message='Webhook already inactive')

        updated_server = await self._webhook_repo.update(
            column=ColumnEnum.ID,
            value=existing.id,
            data={ColumnEnum.SERVER_STATUS: ServerStatusEnum.INACTIVE}
        )
        logger.info(f"[WebhookService]: Deactivated webhook: {updated_server!r}")
        return updated_server

    async def delete(self, id: UUID, user_id: UUID) -> None:
        existing = await self._webhook_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')


        await self._webhook_repo.delete(column=ColumnEnum.ID, value=id)
        logger.info(f"[WebhookService]: Deleted server: {id}")

    async def retry(self, id: UUID, user_id: UUID) -> WebhookEntity:
        existing = await self._webhook_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        if existing.server_status == ServerStatusEnum.INACTIVE:
            raise ConflictError(message='Webhook already inactive')

        if existing.status != StatusEnum.WAITING:
            existing = await self._webhook_repo.update(
                column=ColumnEnum.ID,
                value=existing.id,
                data={ColumnEnum.STATUS: StatusEnum.WAITING}
            )

        logger.info(f"[WebhookService]: Retry webhook: {existing!r}")
        return existing
