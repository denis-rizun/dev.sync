from fastapi import APIRouter
from starlette.requests import Request

from backend.core.utils import Mapper
from backend.domain.dtos.user import RegistrationDTO
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.user import UserSchema, RegistrationSchema

user_router = APIRouter(prefix="/users", tags=["user"])


@user_router.post(path="/", response_model=UserSchema, status_code=201)
async def registration(request: Request, data: RegistrationSchema) -> UserSchema:
    data_with_location = {**data.model_dump(), "location": request.state.location}
    service = await container.user_service()
    result = await service.registrate(data=RegistrationDTO(**data_with_location))
    return Mapper.to_schema(schema=UserSchema, dto=result)
