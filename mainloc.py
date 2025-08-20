import asyncio
import logging
from bot.handlers import setup_routers
from config_reader import dp, bot

dp.include_router(setup_routers())


async def main():
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
