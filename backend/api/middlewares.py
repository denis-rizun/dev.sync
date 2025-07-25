from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from backend.core.config import config
from backend.core.exceptions import AuthenticationError
from backend.domain.enums.token import JWTTokenType
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.security.jwt_handler import JWTHandler


class DatabaseMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        session = await container.session()
        try:
            response = await call_next(request)
            if request.method not in {"OPTIONS", "GET"}:
                await session.commit()
            return response
        except SQLAlchemyError as e:
            await session.rollback()
            return JSONResponse(
                status_code=409,
                content={"detail": str(e)}
            )
        finally:
            await session.close()


class RequestMetaMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path.endswith("login/"):
            x_forwarded_for = request.headers.get("x-forwarded-for")
            ip = (
                x_forwarded_for.split(",")[0]
                if x_forwarded_for
                else request.client.host
            )
            request.state.ip = ip
            request.state.agent = request.headers.get("user-agent")

        return await call_next(request)


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        if self._is_public_path(request):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.removeprefix("Bearer ").strip()
            try:
                decoded_token = JWTHandler.decode_token(token)
                request.state.user_id = UUID(decoded_token["sub"])
                return await call_next(request)
            except AuthenticationError as e:
                return JSONResponse(
                    status_code=403,
                    content={"detail": str(e)}
                )
        else:
            dev_token = request.cookies.get(JWTTokenType.DEV_TOKEN.value)
            if dev_token and dev_token == str(config.CELERY_AUTH_TOKEN):
                request.state.user_id = config.CELERY_AUTH_USER_ID
                return await call_next(request)

            return JSONResponse(
                status_code=403,
                content={"detail": "Not authenticated"},
            )

    @staticmethod
    def _is_public_path(request: Request) -> bool:
        return (
            request.method == "OPTIONS" or
            request.url.path.startswith("/docs") or
            request.url.path == "/api/openapi.json" or
            request.url.path.endswith("registration/") or
            request.url.path.endswith("login/") or
            request.url.path.endswith("token/") or
            request.url.path.endswith("health/") or
            request.url.path.startswith("/call")
        )
