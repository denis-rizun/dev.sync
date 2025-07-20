from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    server_id: Mapped[int] = mapped_column(ForeignKey('servers.id'))
