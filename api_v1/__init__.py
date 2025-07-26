from fastapi import APIRouter
from .users.views import router as users_router
from .classes.views import router as classes_router
from .marks.views import router as marks_router
router = APIRouter()
router.include_router(router=users_router, prefix="/user")
router.include_router(router=classes_router, prefix="/class")
router.include_router(router=marks_router, prefix="/mark")