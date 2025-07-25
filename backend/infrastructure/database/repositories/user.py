from sqlalchemy import select, or_

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

    async def get_by_username_or_mail(
            self,
            username: str | None,
            mail: str | None
    ) -> UserEntity | None:
        conditions = []

        if username is not None:
            conditions.append(self.MODEL.username == username)

        if mail is not None:
            conditions.append(self.MODEL.mail == mail)

        if not conditions:
            return None

        stmt = select(self.MODEL).where(or_(*conditions))
        result = await self.session.execute(stmt)
        found = result.scalar_one_or_none()

        if found:
            return self.MAPPER.to_entity(found)

        return None
