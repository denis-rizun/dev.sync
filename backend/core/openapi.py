from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from backend.core.config import config


class OpenAPIConfigurator:

    @staticmethod
    def configure(app: FastAPI) -> dict[str, Any]:
        def wrap_openapi():
            if app.openapi_schema:
                return app.openapi_schema

            openapi_schema = get_openapi(
                title=f"{config.PROJECT_NAME} Documentation",
                version=config.VERSION,
                routes=app.routes,
            )
            if "components" not in openapi_schema:
                openapi_schema["components"] = {}

            openapi_schema["components"]["securitySchemes"] = {
                "BearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }

            for path in openapi_schema["paths"].values():
                for method in path.values():
                    method.setdefault("security", [])
                    method["security"].append({"BearerAuth": []})

            app.openapi_schema = openapi_schema
            return app.openapi_schema
        return wrap_openapi
