from datetime import datetime
from typing import Any

from backend.core.config import config
from backend.core.logger import Logger
from backend.domain.enums.common import RequestMethodEnum
from backend.domain.enums.token import JWTTokenType
from backend.infrastructure.tasks.base import BaseTask

logger = Logger.setup_logger(__name__)


class SessionCleanupTask(BaseTask):
    name = "cron.cleanup_sessions"

    def run(self) -> None:
        try:
            sessions = self._get_active_sessions()
            expired_ids = self._filter_expired_sessions(sessions=sessions)
            if not expired_ids:
                logger.info(f"[CeleryTask | {self.name}]: No sessions to deactivate")
                return

            self._deactivate_sessions(ids=expired_ids)
            logger.info(f"[CeleryTask | {self.name}]: Sessions deactivated: {len(expired_ids)}")

        except Exception as e:
            logger.error(f"[CeleryTask | {self.name}]: Cleanup failed: {e}")

    def _get_active_sessions(self) -> list[dict[str, Any]]:
        response = self._request(
            method=RequestMethodEnum.GET,
            url=f"{self.BASE_API_URL}/v1/sessions/",
            cookies={JWTTokenType.DEV_TOKEN: str(config.CELERY_AUTH_TOKEN)}
        )
        return response.json() if response else []

    def _deactivate_sessions(self, ids: list[int]) -> None:
        self._request(
            method=RequestMethodEnum.PATCH,
            url=f"{self.BASE_API_URL}/v1/sessions/",
            cookies={JWTTokenType.DEV_TOKEN: str(config.CELERY_AUTH_TOKEN)},
            params={"ids": ids}
        )

    @classmethod
    def _filter_expired_sessions(cls, sessions: list[dict[str, Any]]) -> list[int]:
        now = datetime.now()
        return [
            session.get("id")
            for session in sessions
            if session.get("expire_time") and session.get("expire_time") < now
        ]
