from datetime import datetime

import google.genai as genai
from django.conf import settings

from .types import ReminderItem, ReminderResponse, RequestCategory, RequestCategoryResponse

client = genai.Client(api_key=settings.GOOGLE_AI_API_KEY)


def get_request_category(text: str) -> RequestCategory:
    prompt = f"Determine what category this text can be."
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            prompt,
            "\n\n",
            text,
        ],
        config={
            "response_mime_type": "application/json",
            "response_schema": RequestCategoryResponse,
        },
    )
    return response.parsed.category


def get_reminder_data(current_time: datetime, message: str) -> list[ReminderItem]:
    prompt = f"Extract all reminder data from the message.\nCurrent time: {current_time}"
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[prompt, "\n\n", message],
        config={
            "response_mime_type": "application/json",
            "response_schema": ReminderResponse,
        },
    )
    return response.parsed.reminders
