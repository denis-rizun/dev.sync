from backend.core.exceptions import DuplicateDataError
from backend.core.logger import Logger
from backend.core.utils import Mapper
from backend.domain.abstractions.repositories import IUserRepository
from backend.domain.abstractions.services.user import IUserService
from backend.domain.dtos.user import RegistrationDTO, LoginDTO
from backend.domain.entities.user import UserEntity
from backend.infrastructure.security.pasword import PasswordHelper

logger = Logger.setup_logger(__name__)


class UserService(IUserService):
    def __init__(self, user_repo: IUserRepository) -> None:
        self._user_repo = user_repo

    async def registrate(self, data: RegistrationDTO) -> UserEntity:
        existing = await self._user_repo.get_by_username_or_mail(
            username=data.username,
            mail=data.mail
        )
        if existing:
            raise DuplicateDataError(message='Username or mail already exists')

        hashed_pwd = PasswordHelper.hash_password(pwd=data.password)
        data.password = hashed_pwd

        entity = Mapper.to_entity(entity=UserEntity, dto=data)
        new_user = await self._user_repo.create(entity=entity)
        logger.info(f"[UserService]: Registered user: {new_user!r}")
        return new_user

    async def login(self, data: LoginDTO) -> UserEntity:
        ...

    async def logout(self):
        ...
