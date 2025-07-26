from typing import Any

from celery import Task
from requests import RequestException

from backend.core.config import config
from backend.core.logger import Logger
from backend.infrastructure.tasks.mixin import RequesterMixin

logger = Logger.setup_logger(__name__)


class BaseTask(Task, RequesterMixin):
    BASE_API_URL = f"http://backend:{config.API_PORT}/api"
    abstract = True
    autoretry_for = (RequestException, Exception)
    retry_kwargs = {"max_retries": 3, "countdown": 10}
    retry_jitter = True

    def on_success(
            self,
            retval: Any,
            task_id: str,
            args: tuple,
            kwargs: dict[str, Any]
    ) -> None:
        logger.info(f"[CeleryTask]: Task {self.name} succeeded: {task_id}")
        super().on_success(retval=retval, task_id=task_id, args=args, kwargs=kwargs)

    def on_failure(
            self,
            exc: Exception,
            task_id: str,
            args: tuple,
            kwargs: dict[str, Any],
            einfo: Any
    ) -> None:
        logger.error(f"[CeleryTask]: Task {self.name} failed: {task_id} — {exc}")
        super().on_failure(exc=exc, task_id=task_id, args=args, kwargs=kwargs, einfo=einfo)
