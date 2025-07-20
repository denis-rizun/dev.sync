from dataclasses import dataclass

from backend.domain.dtos.base import BaseUpdateDTO
from backend.domain.enums.common import StatusEnum, ServerStatusEnum
from backend.domain.enums.webhook import WebhookSourceEnum


@dataclass
class WebhookCreateDTO:
    repository: str
    key: str
    branch: str
    shell: str
    server_id: int
    source: WebhookSourceEnum


@dataclass
class WebhookUpdateDTO(BaseUpdateDTO):
    status: StatusEnum | None = None
    repository: str | None = None
    key: str | None = None
    branch: str | None = None
    shell: str | None = None
    source: WebhookSourceEnum | None = None
    server_status: ServerStatusEnum | None = None
