from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from backend.domain.enums.common import ServerStatusEnum


@dataclass
class ServerEntity:
    id: UUID | None = None
    name: str | None = None
    server_status: ServerStatusEnum | None = None
    user_id: UUID | None = None
    ip: str | None = None
    port: int | None = None
    account: str | None = None
    pkey: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __repr__(self) -> str:
        return f"<Server(id='{self.id}')>"
