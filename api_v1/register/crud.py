from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import random
from api_v1.register.send_message import send_message
from api_v1.users.crud import user_exists
from core.models import Register

async def get_registers(session: AsyncSession) -> list[Register]:
    stmt = select(Register).order_by(Register.email)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def send_code(session: AsyncSession, email: str)-> int:
    if_exists = await user_exists(session, email, "")
    if if_exists == 1:
        return 0
    code = ''.join(random.choices('0123456789', k=6))
    try:
        result = await session.execute(select(Register).where(Register.email == email))
        user = result.scalar_one_or_none()

        if user:
            user.code = int(code)
        else:
            user = Register(email=email, code=int(code))
            session.add(user)

        await session.commit()
        send_message(email, code)
        return int(code)
    except Exception as e:
        await session.rollback()
        print(f"Ошибка: {e}")
        return 0


