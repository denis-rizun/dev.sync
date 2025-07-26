from celery import Celery

from backend.core.config import config
from backend.infrastructure.tasks.callable import WebhookExecutionTask
from backend.infrastructure.tasks.cron import SessionCleanupTask, beat_schedule


class CeleryInitializer:

    @classmethod
    def initialize(cls) -> Celery:
        app = cls._get_celery_app()
        cls._configure(app)
        cls._register_tasks(app)
        return app

    @classmethod
    def _get_celery_app(cls) -> Celery:
        return Celery(
            main=config.PROJECT_NAME,
            broker=config.CELERY_BROKER_URL,
            backend=config.CELERY_BACKEND_URL,
        )

    @classmethod
    def _configure(cls, app: Celery) -> None:
        app.conf.update(
            task_track_started=config.CELERY_TASK_TRACK_STARTED,
            task_time_limit=config.CELERY_TASK_TIME_LIMIT,
            task_soft_time_limit=config.CELERY_TASK_SOFT_TIME_LIMIT,
            timezone=config.CELERY_TIMEZONE,
            enable_utc=config.CELERY_ENABLE_UTC,
        )

        app.conf.beat_schedule = beat_schedule

    @classmethod
    def _register_tasks(cls, app: Celery) -> None:
        app.register_task(WebhookExecutionTask())
        app.register_task(SessionCleanupTask())


celery = CeleryInitializer.initialize()
