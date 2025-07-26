from fastapi import APIRouter
from fastapi.requests import Request

from backend.core.utils import Mapper
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.user import UserSchema

user_router = APIRouter(prefix="/v1/users", tags=["User"])


@user_router.get(path="/me/", response_model=UserSchema, status_code=200)
async def account(request: Request) -> UserSchema:
    service = await container.user_service()
    result = await service.get_account(id=request.state.user_id)
    return Mapper.to_schema(schema=UserSchema, dto=result)
