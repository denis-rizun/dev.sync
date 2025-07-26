from uuid import UUID

from fastapi import APIRouter
from fastapi.requests import Request

from backend.core.utils import Mapper
from backend.domain.dtos.webhook import WebhookCreateDTO, WebhookUpdateDTO, WebhookCallDTO
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.webhook import (
    WebhookCreateSchema,
    WebhookSchema,
    WebhookUpdateSchema,
    WebhookCallSchema
)

webhook_router = APIRouter(prefix="/v1/webhooks", tags=["Webhook"])


@webhook_router.post(path="/", response_model=WebhookSchema, status_code=201)
async def create_webhook(request: Request, data: WebhookCreateSchema) -> WebhookSchema:
    dto = Mapper.to_dto(dto=WebhookCreateDTO, schema=data)
    service = await container.webhook_service()
    result = await service.create(data=dto, user_id=request.state.user_id)
    return Mapper.to_schema(schema=WebhookSchema, dto=result)


@webhook_router.get(path="/", response_model=list[WebhookSchema], status_code=200)
async def get_webhooks(request: Request) -> list[WebhookSchema]:
    service = await container.webhook_service()
    result = await service.get_webhooks(user_id=request.state.user_id)
    return [Mapper.to_schema(schema=WebhookSchema, dto=res) for res in result]


@webhook_router.patch(path="/{id}", response_model=WebhookSchema, status_code=200)
async def update(request: Request, id: UUID, data: WebhookUpdateSchema) -> WebhookSchema:
    dto = Mapper.to_dto(dto=WebhookUpdateDTO, schema=data)
    service = await container.webhook_service()
    result = await service.update(id=id, user_id=request.state.user_id, data=dto)
    return Mapper.to_schema(schema=WebhookSchema, dto=result)


@webhook_router.delete(path="/{id}", response_model=None, status_code=204)
async def delete_webhook(request: Request, id: UUID) -> None:
    service = await container.webhook_service()
    await service.delete(id=id, user_id=request.state.user_id)


@webhook_router.post(path="/{key}", response_model=None, status_code=204)
async def retry_webhook(request: Request, key: str) -> None:
    service = await container.webhook_service()
    result = await service.retry(key=key, user_id=request.state.user_id)
    return Mapper.to_schema(schema=WebhookSchema, dto=result)


@webhook_router.post(path="/call/{key}", response_model=None, status_code=204)
async def call_webhook(key: str, data: WebhookCallSchema) -> None:
    dto = Mapper.to_dto(dto=WebhookCallDTO, schema=data)
    service = await container.webhook_service()
    await service.call(key=key, data=dto)
