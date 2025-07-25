from uuid import UUID

from backend.domain.enums.common import ServerStatusEnum
from backend.infrastructure.schemas.base import DevSyncSchema


class ServerSchema(DevSyncSchema):
    id: UUID
    name: str
    server_status: ServerStatusEnum
    user_id: UUID
    ip: str
    port: int
    account: str
    pkey: str


class ServerCreateSchema(DevSyncSchema):
    name: str
    ip: str
    port: int
    account: str
    pkey: str


class ServerUpdateSchema(DevSyncSchema):
    name: str | None = None
    server_status: ServerStatusEnum | None = None
    ip: str | None = None
    port: int | None = None
    account: str | None = None
    pkey: str | None = None
