from backend.domain.entities.webhook import WebhookEntity
from backend.infrastructure.database.models import WebhookModel
from backend.infrastructure.mappers.base import BaseMapper


class WebhookMapper(BaseMapper[WebhookEntity, WebhookModel]):
    ENTITY = WebhookEntity
    MODEL = WebhookModel