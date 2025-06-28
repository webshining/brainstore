from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from django.utils.translation import gettext as _
from django.utils.translation import override

from bot.keyboards import LangKeyboard
from users.models import User

from ..routes import router


@router.message(Command("lang"))
async def lang_handler(message: Message):
    await message.answer(
        _("Select language:"),
        reply_markup=LangKeyboard.keyboard(),
    )


@router.callback_query(LangKeyboard.filter())
async def lang_callback_handler(
    call: CallbackQuery,
    callback_data: LangKeyboard,
    user: User,
):
    user.language_code = callback_data.lang
    await user.asave(update_fields=["language_code"])
    with override(user.language_code):
        await call.message.edit_text(_("Selected: {}").format(callback_data.lang))
