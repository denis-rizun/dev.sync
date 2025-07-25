from datetime import datetime
from typing import Any
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


class WebhookUpdateSchema(DevSyncSchema):
    status: StatusEnum | None = None
    repository: str | None = None
    key: str | None = None
    branch: str | None = None
    shell: str | None = None
    source: WebhookSourceEnum | None = None
    server_status: ServerStatusEnum | None = None


class PushUserDataSchema(DevSyncSchema):
    name: str | None = None
    username: str | None = None
    email: str | None = None


class PushDataSchema(DevSyncSchema):
    repository: dict[str, Any] = None
    ref: str | None = None
    user: PushUserDataSchema | None = None


class RepositorySchema(DevSyncSchema):
    name: str | None = None


class PusherSchema(DevSyncSchema):
    name: str | None = None
    username: str | None = None
    email: str | None = None


class WebhookCallSchema(DevSyncSchema):
    repository: RepositorySchema | None = None
    push_data: PushDataSchema| None = None
    ref: str | None = None
    pusher: PusherSchema | None = None
    user_name: str | None = None
    user_email: str | None = None
