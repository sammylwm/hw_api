from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from api_v1 import router as api_router
from api.users.views import router as users_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(router=api_router, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
