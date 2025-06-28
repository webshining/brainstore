import os

from celery import Celery, Task

from utils import logger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


class LoggingTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.exception(f"Task failed: {exc}", exc_info=exc)
        super().on_failure(exc, task_id, args, kwargs, einfo)


app = Celery("app")
app.conf.enable_utc = True
app.conf.timezone = "UTC"
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()
