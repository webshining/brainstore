from aiogram.enums import ParseMode
from django.db.models.signals import post_save
from django.dispatch import receiver
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from ai.models import Message
from ai.tasks import process_request
from bot.loader import sync_bot
from bot.signals import process_request_signal


@receiver(process_request_signal)
def _process_request(message: str, user_id: int, *args, **kwargs):
    process_request.delay(message, user_id)


@receiver(post_save, sender=Message)
def _message_post_save(instance: Message, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🆗", callback_data=f"reminder:{instance.id}"))
    sync_bot.send_message(chat_id=instance.user.telegram_id, text=f'```json\n{instance.response}```',
                          reply_markup=markup, parse_mode=ParseMode.MARKDOWN_V2)
