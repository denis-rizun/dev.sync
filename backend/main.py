from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.api.routers import routers
from backend.core.config import config
from backend.api.exception_handlers import ExceptionHandler
from backend.api.middlewares import DatabaseMiddleware, RequestMetaMiddleware, AuthMiddleware
from backend.core.openapi import OpenAPIConfigurator

app = FastAPI(root_path="/api")
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)
app.add_middleware(middleware_class=DatabaseMiddleware)
app.add_middleware(middleware_class=RequestMetaMiddleware)
app.add_middleware(middleware_class=AuthMiddleware)

for router in routers:
    app.include_router(router)

app.openapi = OpenAPIConfigurator.configure(app=app)
ExceptionHandler.register(app=app)
