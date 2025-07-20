from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.domain.enums.common import StatusEnum, ServerStatusEnum
from backend.domain.enums.history import HistoryTriggerEnum
from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class HistoryModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'histories'

    status: Mapped[StatusEnum]
    output: Mapped[str]
    trigger_type: Mapped[HistoryTriggerEnum]

    webhook_id: Mapped[UUID] = mapped_column(ForeignKey("webhooks.id"))
    webhook: Mapped["WebhookModel"] = relationship(back_populates="histories")  # noqa

    server_id: Mapped[UUID] = mapped_column(ForeignKey("servers.id"))
    server: Mapped["ServerModel"] = relationship(back_populates="histories")  # noqa
