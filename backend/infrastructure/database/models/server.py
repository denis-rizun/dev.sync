from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from backend.domain.enums.common import ServerStatusEnum
from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin



class ServerModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'servers'

    name: Mapped[str]
    server_status: Mapped[ServerStatusEnum] = mapped_column(default=ServerStatusEnum.ACTIVE)
    user_id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey('users.id'))
    ip: Mapped[str]
    port: Mapped[int]
    account: Mapped[str]
    pkey: Mapped[str]
