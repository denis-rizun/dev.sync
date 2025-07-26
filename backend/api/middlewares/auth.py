from uuid import UUID

from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from backend.core.config import config
from backend.core.exceptions import AuthenticationError
from backend.domain.enums.token import JWTTokenType
from backend.infrastructure.security.jwt_handler import JWTHandler


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path.endswith("login/"):
            forwarded = request.headers.get("x-forwarded-for")
            ip = forwarded.split(",")[0] if forwarded else request.client.host
            request.state.ip = ip
            request.state.agent = request.headers.get("user-agent")

        if self._is_public_path(request):
            return await call_next(request)

        token = self._extract_token(request)
        if token:
            try:
                payload = JWTHandler.decode_token(token)
                request.state.user_id = UUID(payload["sub"])
                return await call_next(request)
            except AuthenticationError as exc:
                return JSONResponse(status_code=403, content={"detail": str(exc)})

        dev_token = request.cookies.get(JWTTokenType.DEV_TOKEN.value)
        if dev_token == str(config.CELERY_AUTH_TOKEN):
            request.state.user_id = config.CELERY_AUTH_USER_ID
            return await call_next(request)

        return JSONResponse(status_code=403, content={"detail": "Not authenticated"})

    @staticmethod
    def _extract_token(request: Request) -> str | None:
        auth = request.headers.get("Authorization")
        if auth and auth.startswith("Bearer "):
            return auth.removeprefix("Bearer ").strip()
        return None

    @staticmethod
    def _is_public_path(request: Request) -> bool:
        path = request.url.path
        return (
                request.method == "OPTIONS" or
                path.startswith("/docs") or
                path == "/api/openapi.json" or
                any(
                    path.endswith(p)
                    for p in ("registration/", "login/", "token/", "health/")
                ) or
                path.startswith("/call")
        )
