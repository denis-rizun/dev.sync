from datetime import datetime, timedelta

from backend.core.config import config
from backend.core.exceptions import (
    DuplicateDataError,
    CredentialsError,
    NotFoundError,
    AuthenticationError
)
from backend.core.logger import Logger
from backend.core.utils import Mapper
from backend.domain.abstractions.repositories import IUserRepository
from backend.domain.abstractions.repositories.session import ISessionRepository
from backend.domain.abstractions.services.auth import IAuthService
from backend.domain.dtos.auth import RegistrationDTO, LoginDTO, TokenDTO
from backend.domain.entities.session import SessionEntity
from backend.domain.entities.token import TokenEntity
from backend.domain.entities.user import UserEntity
from backend.domain.enums.common import ColumnEnum
from backend.infrastructure.security.jwt_handler import JWTHandler
from backend.infrastructure.security.password import PasswordHelper

logger = Logger.setup_logger(__name__)


class AuthService(IAuthService):
    def __init__(self, user_repo: IUserRepository, session_repo: ISessionRepository) -> None:
        self._user_repo = user_repo
        self._session_repo = session_repo

    async def register(self, data: RegistrationDTO) -> UserEntity:
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
        logger.info(f"[AuthService]: Registered user: {new_user!r}")
        return new_user

    async def login(self, data: LoginDTO) -> TokenEntity:
        existing = await self._user_repo.get_by_username_or_mail(
            username=data.username,
            mail=data.mail
        )
        if not existing:
            raise CredentialsError(message='Credentials are incorrect')

        is_password_correct = PasswordHelper.check_password(
            pwd=data.password,
            hashed_pwd=existing.password
        )
        if not is_password_correct:
            raise CredentialsError(message='Credentials are incorrect')

        token_dto = self._create_tokens(entity=existing)
        new_session = await self._session_repo.create(
            entity=SessionEntity(
                user_id=existing.id,
                refresh_token=token_dto.refresh_token,
                ip=data.location,
                agent=data.agent,
                expired_at=datetime.now() + timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)
            )
        )
        logger.info(f"[AuthService]: Logged in user: {new_session!r}")
        return Mapper.to_entity(entity=TokenEntity, dto=token_dto)

    async def logout(self, id: int, token: str | None) -> None:
        if not token:
            raise AuthenticationError(message="Refresh token missing")

        existing = await self._session_repo.get_active_session(user_id=id, token=token)
        if not existing:
            raise NotFoundError(message='Active session not found')

        await self._session_repo.update(
            column=ColumnEnum.ID,
            value=existing.id,
            data={ColumnEnum.REVOKED: True}
        )
        logger.info(f"[AuthService]: Logged out user: {id}")

    async def refresh_access_token(self, token: str | None) -> TokenEntity:
        if not token:
            raise AuthenticationError(message="Refresh token missing")

        data = JWTHandler.decode_token(token=token)
        existing = await self._user_repo.get_existed(column=ColumnEnum.ID, value=data["sub"])
        access_token = JWTHandler.create_access_token(id=existing.id, username=existing.username)
        return TokenEntity(access_token=access_token)

    @classmethod
    def _create_tokens(cls, entity: UserEntity) -> TokenDTO:
        access_token = JWTHandler.create_access_token(id=entity.id, username=entity.username)
        refresh_token = JWTHandler.create_refresh_token(id=entity.id)
        return TokenDTO(access_token=access_token, refresh_token=refresh_token)
