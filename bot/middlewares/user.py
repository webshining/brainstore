from aiogram.dispatcher.event.telegram import TelegramEventObserver
from aiogram.types import CallbackQuery, InlineQuery, Message
from django.utils.translation import override

from users.services import create_or_update_user


async def user_middleware(event: TelegramEventObserver):
    @event.middleware()
    async def process(handler, event: Message | CallbackQuery | InlineQuery, data):
        await process_user(event.from_user, data)
        with override(data["user"].language_code):
            await handler(event, data)

    async def process_user(from_user, data):
        user = await create_or_update_user(
            from_user.id, from_user.username, from_user.first_name, from_user.last_name, from_user.language_code
        )
        data["user"] = user
