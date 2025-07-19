from uuid import UUID

from fastapi import APIRouter
from starlette.requests import Request

from backend.core.utils import Mapper
from backend.domain.dtos.service import ServerCreateDTO
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.server import ServerSchema, ServerCreateSchema

server_router = APIRouter(prefix="/v1/servers", tags=["Server"])


@server_router.get(path="/", response_model=list[ServerSchema], status_code=200)
async def get_servers_info(request: Request) -> list[ServerSchema]:
    service = await container.server_service()
    result = await service.get_servers_info(user_id=request.state.user_id)
    return [Mapper.to_schema(schema=ServerSchema, dto=res) for res in result]


@server_router.post(path="/", response_model=ServerSchema, status_code=201)
async def create_server(request: Request, data: ServerCreateSchema) -> ServerSchema:
    dto = Mapper.to_dto(dto=ServerCreateDTO, schema=data)
    service = await container.server_service()
    result = await service.create(data=dto, user_id=request.state.user_id)
    return Mapper.to_schema(schema=ServerSchema, dto=result)


@server_router.patch(path="/{id}", response_model=ServerSchema, status_code=200)
async def deactivate(request: Request, id: UUID) -> ServerSchema:
    service = await container.server_service()
    result = await service.deactivate(id=id, user_id=request.state.user_id)
    return Mapper.to_schema(schema=ServerSchema, dto=result)


@server_router.delete(path="/{id}", response_model=None, status_code=204)
async def delete(request: Request, id: UUID) -> None:
    service = await container.server_service()
    return await service.delete(id=id, user_id=request.state.user_id)
