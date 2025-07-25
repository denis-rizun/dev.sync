from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from backend.domain.entities.server import ServerEntity
from backend.domain.enums.common import ServerStatusEnum, StatusEnum
from backend.domain.enums.webhook import WebhookSourceEnum


@dataclass
class WebhookEntity:
    id: UUID | None = None
    status: StatusEnum | None = None
    repository: str | None = None
    key: str | None = None
    branch: str | None = None
    shell: str | None = None
    user_id: int | None = None
    server_id:int | None = None
    source: WebhookSourceEnum | None = None
    server_status: ServerStatusEnum | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __repr__(self) -> str:
        return f"<Webhook(id='{self.id}')>"


@dataclass
class WebhookExtendedEntity(WebhookEntity):
    server: ServerEntity | None = None

    def __repr__(self) -> str:
        return f"<WebhookExtended(id='{self.id}')>"
