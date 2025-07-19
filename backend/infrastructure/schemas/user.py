from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from backend.infrastructure.schemas.base import DevSyncSchema


class UserSchema(DevSyncSchema):
    id: UUID
    username: str | None
    mail: EmailStr | None
    avatar: str
    created_at: datetime
    updated_at: datetime
