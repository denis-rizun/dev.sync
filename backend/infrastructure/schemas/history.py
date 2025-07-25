from uuid import UUID

from backend.domain.enums.common import StatusEnum
from backend.infrastructure.schemas.base import DevSyncSchema


class HistorySchema(DevSyncSchema):
    status: StatusEnum
    output: str
    pusher: str | None
    webhook_id: UUID
    server_id: UUID


class HistoryCreateSchema(DevSyncSchema):
    status: StatusEnum | None = None
    output: str
    pusher: str | None
    webhook_id: UUID
    server_id: UUID

