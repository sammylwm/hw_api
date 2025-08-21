from aiogram import BaseMiddleware
from typing import Callable, Any, Dict, Awaitable
from sqlalchemy.ext.asyncio import AsyncSession

class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_dependency):
        self.session_dependency = session_dependency  # генератор с yield

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any]
    ) -> Any:
        agen = self.session_dependency()  # создаем генератор
        session: AsyncSession = await agen.__anext__()  # первый yield

        try:
            data["session"] = session  # передаем в хендлер
            return await handler(event, data)
        finally:
            try:
                await agen.__anext__()  # выполняем код после yield
            except StopAsyncIteration:
                pass
