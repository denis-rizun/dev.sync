from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from backend.infrastructure.dependencies.container import container


class DatabaseMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        session = await container.session()
        try:
            response = await call_next(request)
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


class IPMiddleware(BaseHTTPMiddleware):

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path.endswith("/users/") and request.method == "POST":
            x_forwarded_for = request.headers.get("x-forwarded-for")
            ip = (
                x_forwarded_for.split(",")[0]
                if x_forwarded_for
                else request.client.host
            )
            request.state.location = ip

        return await call_next(request)
