from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.domain.enums.common import StatusEnum, ServerStatusEnum
from backend.domain.enums.webhook import WebhookSourceEnum
from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class WebhookModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'webhooks'

    status: Mapped[StatusEnum] = mapped_column(default=StatusEnum.WAITING)
    server_status: Mapped[ServerStatusEnum] = mapped_column(default=ServerStatusEnum.ACTIVE)
    repository: Mapped[str] = mapped_column(unique=True)
    key: Mapped[str] = mapped_column(unique=True)
    branch: Mapped[str]
    shell: Mapped[str]
    source: Mapped[WebhookSourceEnum]

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="webhooks")  # noqa

    server_id: Mapped[UUID] = mapped_column(ForeignKey("servers.id"))
    server: Mapped["ServerModel"] = relationship(back_populates="webhooks")  # noqa

    histories: Mapped[list["HistoryModel"]] = relationship(back_populates="webhook")  # noqa
