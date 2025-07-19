from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.routers import routers
from backend.core.config import config
from backend.api.exception_handlers import register_exception_handlers
from backend.api.middlewares import DatabaseMiddleware, IPMiddleware

app = FastAPI(title=f"{config.PROJECT_NAME} API", version=config.VERSION, root_path="/api")
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)
app.add_middleware(middleware_class=DatabaseMiddleware)
app.add_middleware(middleware_class=IPMiddleware)

for router in routers:
    app.include_router(router)

register_exception_handlers(app=app)
