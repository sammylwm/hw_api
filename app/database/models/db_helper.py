from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from asyncio import current_task
from app.database.config import settings


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(
            url=settings.db_url,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def get_scope_session(self):
        session = async_scoped_session(
            self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.get_scope_session() as session:
            yield session
            await session.remove()


db_helper = DatabaseHelper()
