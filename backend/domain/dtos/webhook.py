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


@dataclass
class WebhookCallDTO:
    repository:  dict | None = None
    push_data: dict | None = None
    ref: str | None = None
    pusher: dict | None = None
    user_name: str | None = None
    user_email: str | None = None

    def get_repo_name(self) -> str:
        return (
            self.repository.get("name")
            if self.repository and self.repository.get("name")
            else (
                self.push_data.get("repository").get("name", "")
                if self.push_data and self.push_data.get("repository")
                else ""
            )
        )

    def get_repo_branch(self) -> str:
        ref = self.ref or (self.push_data.get("ref") if self.push_data else "")
        if ref and "/" in ref:
            return ref.rsplit("/", 1)[-1]

        return ref or ""

    def get_push_name(self) -> str | None:
        if self.pusher:
            return self.pusher.get("name") or self.pusher.get("username")

        if self.user_name:
            return self.user_name

        if self.push_data and self.push_data.get("user"):
            return self.push_data.get("user", {}).get("name")

        return None

    def get_push_email(self) -> str | None:
        if self.pusher and self.pusher.get("email"):
            return self.pusher.get("email")

        if self.user_email:
            return self.user_email

        if self.push_data and self.push_data.get("user"):
            return self.push_data.get("user", {}).get("email")

        return None
