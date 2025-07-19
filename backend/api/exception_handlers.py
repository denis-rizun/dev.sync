from fastapi import HTTPException, FastAPI
from starlette.requests import Request

from backend.core.exceptions import DuplicateDataError, AuthenticationError


class ExceptionHandler:

    @staticmethod
    def register(app: FastAPI) -> None:
        @app.exception_handler(DuplicateDataError)
        async def duplication_exception_handler(
                request: Request,
                exc: DuplicateDataError
        ) -> None:
            raise HTTPException(status_code=409, detail=str(exc))

        @app.exception_handler(AuthenticationError)
        async def authentication_exception_handler(
                request: Request,
                exc: DuplicateDataError
        ) -> None:
            raise HTTPException(status_code=403, detail=str(exc))
