from aiogram import F
from aiogram.filters import StateFilter
from aiogram.types import Message, ReactionTypeEmoji

from users.models import User
from ..routes import router
from ...signals import process_request_signal


@router.message(F.text, ~F.text.startswith("/"), StateFilter(None))
async def reminder_text_handler(message: Message, user: User):
    await process_request_signal.asend(None, message=message.text, user_id=user.id)
    await message.react([ReactionTypeEmoji(emoji="👍")])
