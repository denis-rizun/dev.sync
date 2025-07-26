from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

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
            if request.method not in {"GET", "OPTIONS"}:
                await session.commit()

            return response
        except SQLAlchemyError as exc:
            await session.rollback()
            return JSONResponse(status_code=409, content={"detail": str(exc)})
        finally:
            await session.close()
