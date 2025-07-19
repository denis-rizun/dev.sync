from backend.domain.entities.server import ServerEntity
from backend.infrastructure.database.models import ServerModel
from backend.infrastructure.mappers.base import BaseMapper


class ServerMapper(BaseMapper[ServerEntity, ServerModel]):
    ENTITY = ServerEntity
    MODEL = ServerModel
