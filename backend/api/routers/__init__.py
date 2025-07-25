from backend.api.routers.health import health_router
from backend.api.routers.v1.auth import auth_router
from backend.api.routers.v1.history import history_router
from backend.api.routers.v1.server import server_router
from backend.api.routers.v1.session import session_router
from backend.api.routers.v1.user import user_router
from backend.api.routers.v1.webhook import webhook_router

routers = [
    health_router,
    auth_router,
    history_router,
    server_router,
    session_router,
    user_router,
    webhook_router
]
