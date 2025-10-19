from fastapi.middleware.cors import CORSMiddleware
from api_v1 import router as routers_api
from config_reader import app

import uvicorn


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers_api)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
    )
