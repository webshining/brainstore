from django.utils import timezone

from app.celery import app
from reminder.models import Reminder
from users.models import User

from .services import get_reminder_data, get_request_category
from .types import RequestCategory


@app.task()
def process_request(text: str, user_id: int):
    current_time = timezone.now()
    category = get_request_category(text)
    user = User.objects.get(id=user_id)
    if category == RequestCategory.REMINDERS:
        data = get_reminder_data(current_time, text)
        for reminder in data:
            Reminder.objects.create(
                title=reminder.title,
                description=reminder.task,
                is_once=reminder.is_once,
                datetime=reminder.datetime,
                cron=reminder.cron,
                user=user,
            )
