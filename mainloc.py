import asyncio
import logging
from bot.handlers import setup_routers
from bot.middleware import DbSessionMiddleware
from config_reader import dp, bot
from core.models import db_helper

dp.include_router(setup_routers())
dp.message.middleware(DbSessionMiddleware(db_helper.scoped_session_dependency))

async def main():
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
