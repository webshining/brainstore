from django.db import models
from django_celery_beat.models import PeriodicTask

from users.models import User


class Reminder(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    is_once = models.BooleanField(blank=True, null=False, default=True)
    cron = models.CharField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    periodic_task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} [{self.cron if self.cron else self.datetime}]"
