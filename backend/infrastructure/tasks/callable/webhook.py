from typing import Any

from requests import RequestException

from backend.application.ssh import SSHService
from backend.core.config import config
from backend.core.logger import Logger
from backend.domain.dtos.webhook import WebhookCallDTO
from backend.domain.entities.server import ServerEntity
from backend.domain.entities.webhook import WebhookExtendedEntity
from backend.domain.enums.common import StatusEnum, RequestMethodEnum
from backend.domain.enums.token import JWTTokenType
from backend.infrastructure.schemas.history import HistoryCreateSchema
from backend.infrastructure.tasks.base import BaseTask

logger = Logger.setup_logger(__name__)


class WebhookExecutionTask(BaseTask):
    name = "callable.execute_webhook"

    def run(self, webhook_entity_raw: dict[str, Any], data_raw: dict[str, Any]) -> None:
        try:
            webhook_entity = self._build_webhook_entity(webhook_entity_raw)
            data = WebhookCallDTO(**data_raw)

            self._update_webhook_status(
                webhook_id=webhook_entity.id,
                status=StatusEnum.IN_PROGRESS
            )

            ssh_service = self._create_ssh_service(webhook=webhook_entity)
            success, result = ssh_service.execute(script=webhook_entity.shell)
            status = StatusEnum.SUCCESS if success else StatusEnum.ERROR

            self._send_history(webhook_entity, data, result, status)

        except RequestException as e:
            logger.error(f"[CeleryTask | {self.name}]: Request error in webhook task: {e}")
        except Exception as e:
            logger.error(f"[CeleryTask | {self.name}]: General error in webhook task: {e}")

    def _update_webhook_status(self, webhook_id: int, status: StatusEnum) -> None:
        self._request(
            method=RequestMethodEnum.PATCH,
            url=f"{self.BASE_API_URL}/v1/webhooks/{webhook_id}",
            cookies={JWTTokenType.DEV_TOKEN: str(config.CELERY_AUTH_TOKEN)},
            body={"status": status},
            is_raise_for_status=False,
        )

    def _send_history(
            self,
            webhook: WebhookExtendedEntity,
            data: WebhookCallDTO,
            result: str,
            status: StatusEnum,
    ) -> None:
        history = HistoryCreateSchema(
            status=status,
            output=result,
            pusher=data.get_push_name() or data.get_push_email(),
            webhook_id=webhook.id,
            server_id=webhook.server.id,
        )
        self._request(
            method=RequestMethodEnum.POST,
            url=f"{self.BASE_API_URL}/v1/histories/",
            cookies={JWTTokenType.DEV_TOKEN: str(config.CELERY_AUTH_TOKEN)},
            body=history.model_dump(mode="json"),
        )

    @classmethod
    def _build_webhook_entity(cls, raw_entity: dict[str, Any]) -> WebhookExtendedEntity:
        server = ServerEntity(**raw_entity.get("server"))
        entity = WebhookExtendedEntity(**raw_entity)
        entity.server = server
        return entity

    @classmethod
    def _create_ssh_service(cls, webhook: WebhookExtendedEntity) -> SSHService:
        return SSHService(
            ip=webhook.server.ip,
            port=webhook.server.port,
            username=webhook.server.account,
            password_or_key=webhook.server.pkey,
        )
