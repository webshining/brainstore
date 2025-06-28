import google.genai as genai
from aiogram import F
from aiogram.types import Message, ReactionTypeEmoji
from django.conf import settings
from django.utils import timezone

from ai.services import get_reminder_data
from reminder.models import Reminder
from users.models import User

from ..routes import router

client = genai.Client(api_key=settings.GOOGLE_AI_API_KEY)


@router.message(F.voice)
async def reminder_handler(message: Message, user: User):
    current_time = timezone.now()
    file = await message.bot.get_file(message.voice.file_id)
    file_mime = message.voice.mime_type
    file_data = await message.bot.download_file(file.file_path)

    file = client.files.upload(file=file_data, config={"mime_type": file_mime})
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            file,
            "\n\n",
            "Transcribe the audio to text, correct grammar, and add punctuation.",
            "Remove filler words and stutters such as 'эээ', 'ммм', and similar sounds.",
        ],
    )

    data = await get_reminder_data(current_time, response.text)
    for reminder in data.reminders:
        await Reminder.objects.acreate(
            title=reminder.title,
            description=reminder.task,
            cron=reminder.cron,
            datetime=reminder.datetime,
            is_once=reminder.is_once,
            user=user,
        )
    await message.react([ReactionTypeEmoji(emoji="👍")])
