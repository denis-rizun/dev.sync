from uuid import UUID

from fastapi import APIRouter

from backend.core.utils import Mapper
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.session import SessionSchema

session_router = APIRouter(prefix="/v1/sessions", tags=["Session"])


@session_router.patch(path="/", response_model=None, status_code=204)
async def deactivate_sessions(ids: list[UUID]) -> None:
    service = await container.session_service()
    return await service.deactivate(ids=ids)


@session_router.get(path="/", response_model=list[SessionSchema], status_code=200)
async def get_active_sessions() -> list[SessionSchema]:
    service = await container.session_service()
    result = await service.get_active_sessions()
    return [Mapper.to_schema(schema=SessionSchema, dto=res) for res in result]
