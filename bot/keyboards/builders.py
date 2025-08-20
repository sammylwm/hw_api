from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from config_reader import config
from aiogram.types import WebAppInfo
main_markup = (
    InlineKeyboardBuilder()
    .button(text="open", web_app=WebAppInfo(url=config.WEBHOOK_URL))
).as_markup()