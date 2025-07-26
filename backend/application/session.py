from uuid import UUID

from backend.core.logger import Logger
from backend.domain.abstractions.repositories.session import ISessionRepository
from backend.domain.abstractions.services.session import ISessionService
from backend.domain.entities.session import SessionEntity
from backend.domain.enums.common import ColumnEnum

logger = Logger.setup_logger(__name__)


class SessionService(ISessionService):
    def __init__(self, session_repo: ISessionRepository) -> None:
        self._session_repo = session_repo

    async def deactivate(self, ids: list[UUID]) -> None:
        await self._session_repo.update_many(
            column=ColumnEnum.ID,
            values=ids,
            data={ColumnEnum.REVOKED: True}
        )
        logger.info(f"[SessionService]: Deactivated {len(ids)} sessions")

    async def get_active_sessions(self) -> list[SessionEntity]:
        return await self._session_repo.get(
            column=ColumnEnum.REVOKED,
            value=False,
            is_many=True
        )
