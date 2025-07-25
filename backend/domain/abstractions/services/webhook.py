from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.dtos.webhook import WebhookCreateDTO, WebhookUpdateDTO, WebhookCallDTO
from backend.domain.entities.webhook import WebhookEntity


class IWebhookService(ABC):

    @abstractmethod
    async def get_webhooks(self, user_id: UUID) -> list[WebhookEntity | None]:
        pass

    @abstractmethod
    async def create(self, data: WebhookCreateDTO, user_id: UUID) -> WebhookEntity:
        pass

    @abstractmethod
    async def delete(self, id: UUID, user_id: UUID) -> None:
        pass

    @abstractmethod
    async def retry(self, key: str, user_id: UUID) -> WebhookEntity:
        pass

    @abstractmethod
    async def update(
            self,
            id: UUID,
            user_id: UUID,
            data: WebhookUpdateDTO
    ) -> WebhookEntity:
        pass

    @abstractmethod
    async def call(self, key: str, data: WebhookCallDTO) -> None:
        pass
