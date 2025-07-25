from fastapi import APIRouter

from backend.core.utils import Mapper
from backend.domain.dtos.history import HistoryCreateDTO
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.history import HistorySchema, HistoryCreateSchema

history_router = APIRouter(prefix="/v1/histories", tags=["History"])


@history_router.post(path="/", response_model=HistorySchema, status_code=201)
async def create(data: HistoryCreateSchema) -> HistorySchema:
    dto = Mapper.to_dto(dto=HistoryCreateDTO, schema=data)
    service = await container.history_service()
    result = await service.create(data=dto)
    return Mapper.to_schema(schema=HistorySchema, dto=result)
