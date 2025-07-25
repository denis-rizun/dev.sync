from dataclasses import dataclass
from uuid import UUID

from backend.domain.enums.common import StatusEnum


@dataclass
class HistoryCreateDTO:
    output: str
    pusher: str
    webhook_id: UUID
    server_id: UUID
    status: StatusEnum | None = None
