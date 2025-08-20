from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start(ms: Message):
    text = """
        Добро пожаловать. Это телеграм-бот благотворительной организации "Трезвое Дело".
    Вы можете записаться на консультацию с Евгением Леднёвым.  
        """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Записаться на консультацию", callback_data="application"
                )
            ]
        ]
    )
    await ms.answer(text, reply_markup=keyboard)
