from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class SessionModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'sessions'

    refresh_token: Mapped[str] = mapped_column(unique=True, index=True)
    ip: Mapped[str]
    agent: Mapped[str]
    revoked: Mapped[bool] = mapped_column(default=False)
    expired_at: Mapped[datetime]

    user_id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey('users.id'))
    user: Mapped["UserModel"] = relationship(back_populates="sessions")  # noqa
