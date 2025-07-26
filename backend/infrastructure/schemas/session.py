from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SessionSchema(BaseModel):
    id: UUID
    user_id: UUID
    refresh_token: str
    expired_at: datetime
    ip: str
    agent: str
    revoked: bool
    created_at: datetime
    updated_at: datetime
