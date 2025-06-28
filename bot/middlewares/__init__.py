from aiogram import Dispatcher

from .user import user_middleware

middlewares = [user_middleware]


async def setup_middlewares(dp: Dispatcher):
    for middleware in middlewares:
        await middleware(dp.message)
        await middleware(dp.callback_query)
        await middleware(dp.inline_query)


__all__ = ["setup_middlewares"]
