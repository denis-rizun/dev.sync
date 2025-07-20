from datetime import datetime
from typing import Any
from uuid import UUID

from backend.domain.enums.common import ServerStatusEnum, StatusEnum, ColumnEnum
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


class WebhookUpdateSchema(DevSyncSchema):
    status: StatusEnum | None = None
    repository: str | None = None
    key: str | None = None
    branch: str | None = None
    shell: str | None = None
    source: WebhookSourceEnum | None = None
    server_status: ServerStatusEnum | None = None
