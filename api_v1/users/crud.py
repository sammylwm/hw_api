"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User

from .schemas import UserCreate, UserUpdate, UserUpdatePartial


async def user_exists(session: AsyncSession, email: str, password: str) -> int:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
    if not user:
        return 0
    if user.password != password:
        return 1
    return 2


async def get_log_passw_class(session: AsyncSession, email: str) -> list:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
    if not user:
        return []
    return [user.class_name, user.login_dn, user.password_dn]

async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(User)
    return user


async def update_user(
        session: AsyncSession,
        user: User,
        user_update: UserUpdate | UserUpdatePartial,
        partial: bool = False,
) -> User:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return User


async def delete_user(
        session: AsyncSession,
        user: User,
) -> None:
    await session.delete(user)
    await session.commit()
