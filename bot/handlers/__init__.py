from aiogram import Dispatcher

from .user import router


async def setup_routes(dp: Dispatcher):
    dp.include_routers(router)


__all__ = ["setup_routes"]
