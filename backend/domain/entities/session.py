from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class SessionEntity:
    id: UUID | None = None
    user_id: UUID | None = None
    refresh_token: str | None = None
    expired_at: datetime | None = None
    ip: str | None = None
    agent: str | None = None
    revoked: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __repr__(self) -> str:
        return f"<Session(id='{self.id}')>"
