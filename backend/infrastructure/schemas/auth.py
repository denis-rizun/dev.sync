from typing import Self, Any

from pydantic import EmailStr, model_validator

from backend.core.exceptions import ValidationError
from backend.infrastructure.schemas.base import DevSyncSchema


class RegistrationSchema(DevSyncSchema):
    username: str | None = None
    mail: EmailStr | None = None
    password: str

    @model_validator(mode="before")
    def fill_username_from_mail(cls, data: dict[str, Any]):  # noqa
        if data.get("username") is None and data.get("mail"):
            data["username"] = data["mail"].split("@")[0]
        return data

    @model_validator(mode="after")
    def at_least_one_identifier(self) -> Self:
        if not self.username and not self.mail:
            raise ValidationError(message="Either 'username' or 'mail' must be provided")
        return self


class LoginSchema(RegistrationSchema):
    pass


class TokenSchema(DevSyncSchema):
    token_type: str = "Bearer"
    access_token: str
