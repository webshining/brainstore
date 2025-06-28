from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from django.conf import settings
from telebot import TeleBot

bot = Bot(
    settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True)
)
sync_bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
