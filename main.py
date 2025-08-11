from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from api_v1 import router as api_router
from core.config import settings

app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(router=api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
