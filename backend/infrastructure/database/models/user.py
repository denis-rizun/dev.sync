from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class UserModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    mail: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str] = mapped_column(default='https://i.imgur.com/NTknVfT.jpeg')

    webhooks: Mapped[list['WebhookModel']] = relationship(  # noqa
        back_populates="user",
        cascade="all, delete-orphan",
    )
    servers: Mapped[list['ServerModel']] = relationship(  # noqa
        back_populates="user",
        cascade="all, delete-orphan",
    )
    sessions: Mapped[list['SessionModel']] = relationship(  # noqa
        back_populates="user",
        cascade="all, delete-orphan",
    )
