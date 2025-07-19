from backend.core.exceptions import NotFoundError
from backend.core.logger import Logger
from backend.domain.abstractions.repositories import IUserRepository
from backend.domain.abstractions.services.user import IUserService
from backend.domain.entities.user import UserEntity
from backend.domain.enums.common import ColumnEnum

logger = Logger.setup_logger(__name__)


class UserService(IUserService):
    def __init__(self, user_repo: IUserRepository) -> None:
        self._user_repo = user_repo

    async def get_account(self, id: int) -> UserEntity:
        existing = await self._user_repo.get(column=ColumnEnum.ID, value=id)
        if not existing:
            raise NotFoundError(message='User not found')

        return existing
