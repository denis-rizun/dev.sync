from backend.api.routers.health import health_router
from backend.api.routers.v1.auth import auth_router
from backend.api.routers.v1.server import server_router
from backend.api.routers.v1.user import user_router

routers = [health_router, auth_router, server_router, user_router,]
