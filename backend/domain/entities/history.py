from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from backend.domain.enums.common import StatusEnum, ServerStatusEnum
from backend.domain.enums.history import HistoryTriggerEnum


@dataclass
class HistoryEntity:
    id: UUID | None = None
    status: StatusEnum | None = None
    output: str | None = None
    trigger_type: HistoryTriggerEnum | None = None
    webhook_id: UUID | None = None
    server_id: UUID | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __repr__(self) -> str:
        return f"<History(id='{self.id}')>"
