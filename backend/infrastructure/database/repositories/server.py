from backend.domain.abstractions.repositories.server import IServerRepository
from backend.domain.entities.server import ServerEntity
from backend.infrastructure.database.models import ServerModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.server import ServerMapper


class ServerRepository(
    BaseRepository[ServerModel, ServerEntity, ServerMapper],
    IServerRepository[ServerModel, ServerEntity, ServerMapper]
):
    MODEL = ServerModel
    MAPPER = ServerMapper
