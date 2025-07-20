from dataclasses import dataclass

from backend.domain.dtos.base import BaseUpdateDTO
from backend.domain.enums.common import ServerStatusEnum


@dataclass
class ServerCreateDTO:
    name: str
    ip: str
    port: int
    account: str
    pkey: str


@dataclass
class ServerUpdateDTO(BaseUpdateDTO):
    name: str | None = None
    ip: str | None = None
    port: int | None = None
    account: str | None = None
    pkey: str | None = None
    server_status: ServerStatusEnum | None = None
