from sqlalchemy.orm import mapped_column, Mapped

from backend.infrastructure.database.models import Base
from backend.infrastructure.database.models.mixins import IDMixin, TimestampMixin


class UserModel(Base, IDMixin, TimestampMixin):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    mail: Mapped[str] = mapped_column(unique=True)
    avatar: Mapped[str] = mapped_column(default='https://i.imgur.com/NTknVfT.jpeg')
