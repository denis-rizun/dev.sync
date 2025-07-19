from fastapi import HTTPException, FastAPI
from starlette.requests import Request

from backend.core.exceptions import DuplicateDataError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DuplicateDataError)
    async def duplication_exception_handler(
            request: Request,
            exc: DuplicateDataError
    ) -> None:
        raise HTTPException(status_code=409, detail=str(exc))
