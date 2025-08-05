from sqlalchemy.ext.asyncio import AsyncSession
import random
from api_v1.register.send_message import send_message
from api_v1.users.crud import user_exists

async def send_code(session: AsyncSession, email: str)-> int:
    if_exists = await user_exists(session, email, "")
    if if_exists == 1:
        return 0
    code = ''.join(random.choices('123456789', k=6))
    try:
        send_message(email, code)
        return int(code)
    except Exception as e:
        await session.rollback()
        print(f"Ошибка: {e}")
        return 0


