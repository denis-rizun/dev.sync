from dataclasses import asdict
from uuid import UUID

from backend.core.exceptions import NotFoundError, PermissionDeniedError, ConflictError
from backend.core.logger import Logger
from backend.core.utils import Mapper
from backend.domain.abstractions.repositories.server import IServerRepository
from backend.domain.abstractions.repositories.webhook import IWebhookRepository
from backend.domain.abstractions.services.webhook import IWebhookService
from backend.domain.dtos.webhook import WebhookCreateDTO, WebhookUpdateDTO, WebhookCallDTO
from backend.domain.entities.webhook import WebhookEntity, WebhookExtendedEntity
from backend.domain.enums.common import ColumnEnum, ServerStatusEnum
from backend.infrastructure.tasks.callable.webhook import WebhookExecutionTask

logger = Logger.setup_logger(__name__)


class WebhookService(IWebhookService):
    def __init__(self, webhook_repo: IWebhookRepository, server_repo: IServerRepository) -> None:
        self._webhook_repo = webhook_repo
        self._server_repo = server_repo

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

    async def delete(self, id: UUID, user_id: UUID) -> None:
        existing = await self._webhook_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        await self._webhook_repo.delete(column=ColumnEnum.ID, value=id)
        logger.info(f"[WebhookService]: Deleted server: {id}")

    async def retry(self, key: str, user_id: UUID) -> WebhookExtendedEntity:
        existing = await self._webhook_repo.get_with_server(key=key)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        if existing.server_status == ServerStatusEnum.INACTIVE:
            raise ConflictError(message='Webhook already inactive')

        # if existing.status != StatusEnum.WAITING:
        #     existing = await self._webhook_repo.update(
        #         column=ColumnEnum.ID,
        #         value=existing.id,
        #         data={ColumnEnum.STATUS: StatusEnum.WAITING}
        #     )

        server = asdict(existing.server)
        webhook = asdict(existing)
        webhook["server"] = server

        WebhookExecutionTask().delay(webhook, {})
        logger.info(f"[WebhookService]: Retry webhook: {existing!r}")
        return existing

    async def update(self, id: UUID, user_id: UUID, data: WebhookUpdateDTO) -> WebhookEntity:
        existing = await self._webhook_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if str(existing.user_id) != str(user_id):
            raise PermissionDeniedError(message='Permission denied')

        updated_webhook = await self._webhook_repo.update(
            column=ColumnEnum.ID,
            value=id,
            data=data.to_raw()
        )
        logger.info(f"[WebhookService]: Updated webhook: {updated_webhook!r}")
        return updated_webhook

    async def call(self, key: str, data: WebhookCallDTO) -> None:
        existing = await self._webhook_repo.get_with_server(key=key)
        if not existing:
            raise NotFoundError(message='Webhook not found')

        if existing.branch != data.get_repo_branch():
            raise ConflictError(message='Webhook branch does not match')

        if existing.repository != data.get_repo_name():
            raise ConflictError(message='Webhook repo does not match')

        server = asdict(existing.server)
        webhook = asdict(existing)
        webhook["server"] = server

        WebhookExecutionTask().delay(webhook, asdict(data))
        logger.info(f"[WebhookService]: Added webhook to queue: {existing!r}")
