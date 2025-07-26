from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class CollaboratorModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'collaborators'

    webhook_id: Mapped[int] = mapped_column(ForeignKey('webhooks.id'))
    webhook: Mapped['Webhook'] = relationship(argument='Webhook')  # noqa

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(argument='User')  # noqa

    def __repr__(self) -> str:
        return f"<Collaborator(id='{self.id}', webhook_id='{self.webhook_id}')>"
