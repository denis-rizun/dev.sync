from celery.schedules import crontab

beat_schedule = {
    "cleanup-sessions-every-hour": {
        "task": "cron.cleanup_sessions",
        "schedule": crontab(minute=0),
    },
}
