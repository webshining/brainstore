import google.genai as genai
from aiogram import F
from aiogram.types import Message, ReactionTypeEmoji
from django.conf import settings
from django.utils import timezone

from ai.tasks import process_request
from reminder.models import Reminder
from users.models import User

from ..routes import router

client = genai.Client(api_key=settings.GOOGLE_AI_API_KEY)


@router.message(F.text)
async def reminder_text_handler(message: Message, user: User):
    process_request.delay(message.text, user.id)
    await message.react([ReactionTypeEmoji(emoji="👍")])
