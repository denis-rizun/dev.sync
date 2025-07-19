from dataclasses import dataclass


@dataclass
class TokenEntity:
    token_type: str = "Bearer"
    access_token: str | None = None
    refresh_token: str | None = None
