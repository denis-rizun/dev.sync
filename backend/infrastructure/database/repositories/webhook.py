from sqlalchemy import select
from sqlalchemy.orm import joinedload

from backend.domain.abstractions.repositories.webhook import IWebhookRepository
from backend.domain.entities.webhook import WebhookEntity, WebhookExtendedEntity
from backend.infrastructure.database.models import WebhookModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.webhook import WebhookMapper


class WebhookRepository(
    BaseRepository[WebhookModel, WebhookEntity, WebhookMapper],
    IWebhookRepository[WebhookModel, WebhookEntity, WebhookMapper]
):
    MODEL = WebhookModel
    MAPPER = WebhookMapper

    async def get_with_server(self, key: str) -> WebhookExtendedEntity | None:
        stmt = (
            select(self.MODEL)
            .where(self.MODEL.key == key)
            .options(joinedload(self.MODEL.server))
        )
        result = await self.session.execute(stmt)
        raw = result.scalar_one_or_none()
        return self.MAPPER.to_entity_with_server(model=raw) if raw else None
