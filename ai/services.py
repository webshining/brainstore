from datetime import datetime

import google.genai as genai
from django.conf import settings

from ai.types import AIResponse, AIReminder, AICategory

client = genai.Client(api_key=settings.GOOGLE_AI_API_KEY)


def get_request_category(
        text: str,
) -> AICategory:
    prompt = "Determine what category this text can be."
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            prompt,
            text,
        ],
        config={
            'response_mime_type': 'text/x.enum',
            "response_schema": AICategory,
        },
    )
    return response.parsed


def get_reminder_data(current_time: datetime, message: str) -> AIResponse[AIReminder]:
    prompt = "Extract all reminder data from the message."
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[prompt, f"Current time: {current_time}", message],
        config={
            "response_mime_type": "application/json",
            "response_schema": AIReminder,
        },
    )
    return AIResponse(
        prompt=prompt,
        request=message,
        response=response.parsed,
    )
