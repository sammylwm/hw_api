from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from api.users.views import router as users_router
from core.models import Base
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
