from dataclasses import dataclass

from backend.domain.enums.webhook import WebhookSourceEnum


@dataclass
class WebhookCreateDTO:
    repository: str
    key: str
    branch: str
    shell: str
    server_id: int
    source: WebhookSourceEnum
