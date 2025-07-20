from uuid import UUID

from backend.domain.enums.common import StatusEnum
from backend.domain.enums.history import HistoryTriggerEnum
from backend.infrastructure.schemas.base import DevSyncSchema


class HistorySchema(DevSyncSchema):
    status: StatusEnum
    output: str
    trigger_type: HistoryTriggerEnum
    webhook_id: UUID
    server_id: UUID


class HistoryUpdateSchema(DevSyncSchema):
    status: StatusEnum | None = None
