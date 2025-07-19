from dataclasses import dataclass


@dataclass
class RegistrationDTO:
    password: str
    username: str | None = None
    mail: str | None = None
    location: str | None = None


@dataclass
class LoginDTO:
    password: str
    username: str | None = None
    mail: str | None = None
