from aiogram import F
from aiogram.types import Message, ReactionTypeEmoji

from bot.signals import process_request_signal
from users.models import User
from ..routes import router


@router.message(F.text)
async def reminder_text_handler(message: Message, user: User):
    await process_request_signal.asend(None, message=message.text, user_id=user.id)
    await message.react([ReactionTypeEmoji(emoji="👍")])
