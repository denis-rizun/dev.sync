from dataclasses import dataclass


@dataclass
class RegistrationDTO:
    password: str
    username: str | None = None
    mail: str | None = None


@dataclass
class LoginDTO:
    password: str
    username: str | None = None
    mail: str | None = None
    location: str | None = None
    agent: str | None = None


@dataclass
class TokenDTO:
    token_type: str = "Bearer"
    access_token: str | None = None
    refresh_token: str | None = None
