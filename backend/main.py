from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api import routers
from backend.core.config import config

app = FastAPI(title="dev.sync API", version="0.1.0", root_path="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)

for router in routers:
    app.include_router(router)
