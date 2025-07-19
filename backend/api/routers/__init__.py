from backend.api.routers.health import health_router
from backend.api.routers.v1.user import user_router

routers = [health_router, user_router,]
