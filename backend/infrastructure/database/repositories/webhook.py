from backend.domain.abstractions.repositories.webhook import IWebhookRepository
from backend.domain.entities.webhook import WebhookEntity
from backend.infrastructure.database.models import WebhookModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.webhook import WebhookMapper


class WebhookRepository(
    BaseRepository[WebhookModel, WebhookEntity, WebhookMapper],
    IWebhookRepository[WebhookModel, WebhookEntity, WebhookMapper]
):
    MODEL = WebhookModel
    MAPPER = WebhookMapper
