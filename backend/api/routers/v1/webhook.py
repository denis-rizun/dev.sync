from uuid import UUID

from fastapi import APIRouter
from starlette.requests import Request

from backend.core.utils import Mapper
from backend.domain.dtos.webhook import WebhookCreateDTO
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.webhook import WebhookCreateSchema, WebhookSchema

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
async def deactivate_webhook(request: Request, id: UUID) -> WebhookSchema:
    service = await container.webhook_service()
    result = await service.deactivate(id=id, user_id=request.state.user_id)
    return Mapper.to_schema(schema=WebhookSchema, dto=result)


@webhook_router.delete(path="/{id}", response_model=None, status_code=204)
async def delete_webhook(request: Request, id: UUID) -> None:
    service = await container.webhook_service()
    await service.delete(id=id, user_id=request.state.user_id)


@webhook_router.post(path="/{id}", response_model=WebhookSchema, status_code=200)
async def retry_webhook(request: Request, id: UUID) -> WebhookSchema:
    ...
