from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from backend.domain.enums.common import ServerStatusEnum
from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin



class ServerModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'servers'

    name: Mapped[str]
    server_status: Mapped[ServerStatusEnum] = mapped_column(default=ServerStatusEnum.ACTIVE)
    ip: Mapped[str]
    port: Mapped[int]
    account: Mapped[str]
    pkey: Mapped[str]

    user_id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="servers")  # noqa
    webhooks: Mapped[list["WebhookModel"]] = relationship(back_populates="server")  # noqa
    histories: Mapped[list["HistoryModel"]] = relationship(back_populates="server")  # noqa
