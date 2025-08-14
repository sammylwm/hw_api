from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
import crypto
from .schemas import UserCreate, UserUpdate, UserUpdatePartial


async def user_exists(session: AsyncSession, email: str, password: str) -> int:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
    if not user:
        return 0
    if not password:
        return 1
    if password != crypto.unencrypt(user.password):
        return 1
    return 2


async def get_log_passw_class(session: AsyncSession, email: str) -> list:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
    if not user:
        return []
    return [user.class_name, crypto.unencrypt(user.login_dn), crypto.unencrypt(user.password_dn)]

async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.email)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def create_user(session: AsyncSession, user_in: UserCreate) -> bool:
    try:
        user = User(**user_in.model_dump())
        user.password = crypto.encrypt(user.password)
        user.login_dn = crypto.encrypt(user.login_dn)
        user.password_dn = crypto.encrypt(user.password_dn)
        session.add(user)
        await session.commit()
        return True
    except Exception as e:
        print("Error creating user:", e)
        return False


async def delete_user(
        session: AsyncSession,
        email: str,
) -> None:
    user = await session.get(User, email)
    await session.delete(user)
    await session.commit()
