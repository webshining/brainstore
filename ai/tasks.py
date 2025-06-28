from django.utils import timezone

from app.celery import app
from reminders.models import Reminder
from users.models import User
from .services import (
    get_reminder_data,
    get_request_category,
)
from .types import RequestCategory


@app.task()
def process_request(text: str, user_id: int):
    current_time = timezone.now()
    user = User.objects.get(id=user_id)
    category = get_request_category(text)
    if category in (RequestCategory.REMINDERS, RequestCategory.CALENDAR):
        data = get_reminder_data(current_time, text, category.value)
        for reminder in data:
            Reminder.objects.create(
                title=reminder.title,
                message=reminder.message,
                is_once=reminder.is_once,
                datetime=reminder.datetime,
                cron=reminder.cron,
                user=user,
            )
