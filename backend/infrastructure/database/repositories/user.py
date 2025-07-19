from sqlalchemy import select

from backend.domain.abstractions.repositories import IUserRepository
from backend.domain.entities.user import UserEntity
from backend.infrastructure.database.models.user import UserModel
from backend.infrastructure.database.repositories.base import BaseRepository
from backend.infrastructure.mappers.user import UserMapper


class UserRepository(
    BaseRepository[UserModel, UserEntity, UserMapper],
    IUserRepository[UserModel, UserEntity, UserMapper]
):
    MODEL = UserModel
    MAPPER = UserMapper

    async def get_by_username_or_mail(self, username: str, mail: str) -> UserModel | None:
        stmt = (
            select(self.MODEL)
            .where((self.MODEL.username == username) | (self.MODEL.mail == mail))
        )
        result = await self.session.execute(stmt)
        found = result.scalar_one_or_none()
        if found:
            return self.MAPPER.to_entity(found)

        return None
