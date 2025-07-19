from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

from backend.core.exceptions import AuthenticationError
from backend.core.utils import Mapper
from backend.domain.dtos.auth import RegistrationDTO, LoginDTO
from backend.domain.enums.token import JWTTokenType
from backend.infrastructure.dependencies.container import container
from backend.infrastructure.schemas.auth import RegistrationSchema, LoginSchema, TokenSchema
from backend.infrastructure.schemas.user import UserSchema

auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserSchema, status_code=201)
async def registration(data: RegistrationSchema) -> UserSchema:
    dto = Mapper.to_dto(dto=RegistrationDTO, schema=data)
    service = await container.auth_service()
    result = await service.register(data=dto)
    return Mapper.to_schema(schema=UserSchema, dto=result)


@auth_router.post(path="/login/", response_model=TokenSchema, status_code=200)
async def login(request: Request, data: LoginSchema, response: Response) -> TokenSchema:
    dto = Mapper.to_dto(dto=LoginDTO, schema=data)
    dto.location = request.state.ip
    dto.agent = request.state.agent

    service = await container.auth_service()
    result = await service.login(data=dto)
    response.set_cookie(key=JWTTokenType.REFRESH, value=result.refresh_token, httponly=True)
    return Mapper.to_schema(schema=TokenSchema, dto=result)


@auth_router.patch(path="/logout/", response_model=None, status_code=204)
async def logout(request: Request, response: Response) -> None:
    service = await container.auth_service()
    await service.logout(id=request.state.user_id, token=request.cookies.get(JWTTokenType.REFRESH))
    response.delete_cookie(key=JWTTokenType.REFRESH)



@auth_router.post(path="/token/", response_model=TokenSchema, status_code=200)
async def refresh_access_token(request: Request) -> TokenSchema:
    service = await container.auth_service()
    result = await service.refresh_access_token(token=request.cookies.get(JWTTokenType.REFRESH))
    return Mapper.to_schema(schema=TokenSchema, dto=result)
