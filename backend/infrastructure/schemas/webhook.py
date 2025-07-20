from datetime import datetime
from uuid import UUID

from backend.domain.enums.common import ServerStatusEnum, StatusEnum
from backend.domain.enums.webhook import WebhookSourceEnum
from backend.infrastructure.schemas.base import DevSyncSchema


class WebhookSchema(DevSyncSchema):
    id: UUID
    status: StatusEnum
    repository: str
    key: str
    branch: str
    shell: str
    source: WebhookSourceEnum
    server_status: ServerStatusEnum
    user_id: UUID
    server_id: UUID
    created_at: datetime
    updated_at: datetime


class WebhookCreateSchema(DevSyncSchema):
    repository: str
    key: str
    branch: str
    shell: str
    source: WebhookSourceEnum
    server_id: UUID
