from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.dtos.webhook import WebhookCreateDTO
from backend.domain.entities.webhook import WebhookEntity


class IWebhookService(ABC):

    @abstractmethod
    async def get_webhooks(self, user_id: UUID) -> list[WebhookEntity | None]:
        pass

    @abstractmethod
    async def create(self, data: WebhookCreateDTO, user_id: UUID) -> WebhookEntity:
        pass

    @abstractmethod
    async def deactivate(self, id: UUID, user_id: UUID) -> WebhookEntity:
        pass

    @abstractmethod
    async def delete(self, id: UUID, user_id: UUID) -> None:
        pass

    @abstractmethod
    async def retry(self, id: UUID, user_id: UUID) -> ...:
        pass
