import json

from django.utils import timezone

from app.celery import app
from users.models import User
from .services import get_request_category, get_reminder_data
from .types import AICategory


@app.task()
def process_request(text: str, user_id: int):
    current_time = timezone.now()
    user = User.objects.get(id=user_id)
    category = get_request_category(text)
    if category == AICategory.REMINDER:
        data = get_reminder_data(current_time, text)
        user.responses.create(prompt=data.prompt, request=data.request,
                              response=json.loads(data.response.model_dump_json()),
                              category=category)
