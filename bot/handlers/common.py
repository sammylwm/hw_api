from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User

router = Router()


@router.message(CommandStart())
async def start(ms: Message, **data):
    session: AsyncSession = data["session"]
    res = await session.execute(select(User))
    users = res.scalars().first()
    await ms.answer(users.email or "Пользователи не найдены")
