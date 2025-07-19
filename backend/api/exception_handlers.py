from fastapi import HTTPException, FastAPI
from starlette.requests import Request

from backend.core.exceptions import (
    DuplicateDataError,
    AuthenticationError,
    ValidationError,
    NotFoundError
)


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

        @app.exception_handler(ValidationError)
        async def validation_exception_handler(
                request: Request,
                exc: ValidationError
        ) -> None:
            raise HTTPException(status_code=400, detail=str(exc))

        @app.exception_handler(NotFoundError)
        async def not_found_exception_handler(
                request: Request,
                exc: ValidationError
        ) -> None:
            raise HTTPException(status_code=404, detail=str(exc))



