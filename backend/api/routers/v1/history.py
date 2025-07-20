from uuid import UUID

from fastapi import APIRouter
from starlette.requests import Request

from backend.core.utils import Mapper
from backend.domain.dtos.history import HistoryUpdateDTO
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.history import HistorySchema, HistoryUpdateSchema

history_router = APIRouter(prefix="/v1/histories", tags=["History"])


@history_router.patch(path="/{id}", response_model=HistorySchema, status_code=200)
async def update(request: Request, id: UUID, data: HistoryUpdateSchema) -> HistorySchema:
    dto = Mapper.to_dto(dto=HistoryUpdateDTO, schema=data)
    service = await container.history_service()
    result = await service.update(id=id, user_id=request.state.user_id, data=dto)
    return Mapper.to_schema(schema=HistorySchema, dto=result)
