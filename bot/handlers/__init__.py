from aiogram import Router
from . import common, date, day_time, pay, reg_fsm


def setup_routers() -> Router:
    router = Router()
    router.include_router(common.router)
    router.include_router(date.router)
    router.include_router(day_time.router)
    router.include_router(pay.router)
    router.include_router(reg_fsm.router)
    return router
