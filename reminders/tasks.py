from app.celery import app
from bot.loader import sync_bot
from .models import Reminder


@app.task()
def notify(reminder_id: int):
    reminder = Reminder.objects.get(id=reminder_id)

    if reminder.user.telegram_id:
        sync_bot.send_message(
            chat_id=reminder.user.telegram_id,
            text=reminder.title,
        )
