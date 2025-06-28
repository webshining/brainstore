from datetime import datetime

import google.genai as genai
from django.conf import settings

from .types import ReminderResponse

client = genai.Client(api_key=settings.GOOGLE_AI_API_KEY)




async def get_reminder_data(current_time: datetime, message: str) -> ReminderResponse:
    prompt = f"Extract all reminder data from the message.\nCurrent time: {current_time}"
    response = await client.aio.models.generate_content(
        model="gemini-1.5-flash",
        contents=[prompt, "\n\n", message],
        config={
            "response_mime_type": "application/json",
            "response_schema": ReminderResponse,
        },
    )
    return response.parsed
