import json

from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule, ClockedSchedule

from .models import Reminder


@receiver(post_delete, sender=Reminder)
def _reminder_post_delete(instance: Reminder, **kwargs):
    if instance.periodic_task:
        instance.periodic_task.delete()


@receiver(post_save, sender=Reminder)
async def _reminder_post_save(instance: Reminder, **kwargs):
    if instance.periodic_task:
        return

    data = {}
    if instance.cron:
        minute, hout, day_of_month, month_of_year, day_of_weak = instance.cron.split()
        schedule, _ = await CrontabSchedule.objects.aget_or_create(
            minute=minute,
            hour=hout,
            day_of_month=day_of_month,
            month_of_year=month_of_year,
            day_of_week=day_of_weak,
            timezone=settings.TIME_ZONE,
        )
        data["crontab"] = schedule
    else:
        schedule, _ = await ClockedSchedule.objects.aget_or_create(clocked_time=instance.datetime)
        data["clocked"] = schedule
        data["one_off"] = True
    periodic_task = await PeriodicTask.objects.acreate(
        name=f"Reminder: task {instance.id}", task="reminders.tasks.notify", **data, args=json.dumps([instance.id])
    )
    instance.periodic_task = periodic_task
    await instance.asave()
