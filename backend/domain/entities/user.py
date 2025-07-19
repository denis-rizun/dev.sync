from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class UserEntity:
    id: UUID | None = None
    username: str | None = None
    mail: str | None = None
    password: str | None = None
    location: str | None = None
    avatar: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __repr__(self) -> str:
        return f"<User(id='{self.id}')>"
