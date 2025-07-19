from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from backend.infrastructure.schemas.base import DevSyncSchema


class RegistrationSchema(DevSyncSchema):
    username: str | None = None
    mail: EmailStr | None = None
    password: str
    location: str | None = None

    # @model_validator
    # def at_least_one_identifier(cls, values: dict[str, str]) -> dict[str, str]:
    #     username, mail = values.get("username"), values.get("mail")
    #     if not username and not mail:
    #         raise ValueError("Either 'username' or 'mail' must be provided.")
    #     return values

class LoginSchema(DevSyncSchema):
    username: str | None = None
    mail: EmailStr | None = None
    password: str


class UserSchema(DevSyncSchema):
    id: UUID
    username: str
    mail: EmailStr
    location: str
    avatar: str
    created_at: datetime
    updated_at: datetime
