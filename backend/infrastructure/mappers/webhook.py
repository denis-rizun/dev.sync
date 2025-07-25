from backend.domain.entities.webhook import WebhookEntity, WebhookExtendedEntity
from backend.infrastructure.database.models import WebhookModel
from backend.infrastructure.mappers.base import BaseMapper
from backend.infrastructure.mappers.server import ServerMapper


class WebhookMapper(BaseMapper[WebhookEntity, WebhookModel]):
    ENTITY = WebhookEntity
    MODEL = WebhookModel

    @classmethod
    def to_entity_with_server(cls, model: WebhookModel) -> WebhookExtendedEntity:
        data = {k: getattr(model, k) for k in model.__dict__ if not k.startswith('_')}

        if hasattr(model, "server") and model.server:
            data["server"] = ServerMapper.to_entity(model.server)

        return WebhookExtendedEntity(**data)
