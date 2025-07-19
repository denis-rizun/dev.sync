from backend.domain.entities.user import UserEntity
from backend.infrastructure.database.models.user import UserModel
from backend.infrastructure.mappers.base import BaseMapper


class UserMapper(BaseMapper[UserEntity, UserModel]):
    ENTITY = UserEntity
    MODEL = UserModel
