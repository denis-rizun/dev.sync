from datetime import datetime, timedelta
from typing import Any
from uuid import uuid4

from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError

from backend.core.config import config
from backend.core.exceptions import TokenExpiredError, SignatureError
from backend.domain.enums.token import JWTTokenType


class JWTHandler:

    @staticmethod
    def create_access_token(id: int, username: str) -> str:
        now = datetime.now()
        payload = {
            "sub": str(id),
            "type": JWTTokenType.ACCESS,
            "username": username,
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()),
            "jti": str(uuid4()),
        }
        return encode(payload=payload, key=config.private_key, algorithm=config.ALGORITHM)

    @staticmethod
    def create_refresh_token(id: int) -> str:
        now = datetime.now()
        payload = {
            "sub": str(id),
            "type": JWTTokenType.REFRESH,
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=config.REFRESH_TOKEN_EXPIRE_MINUTES)).timestamp()),
            "jti": str(uuid4()),
        }
        return encode(payload=payload, key=config.private_key, algorithm=config.ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> dict[str, Any]:
        try:
            return decode(
                jwt=token,
                key=config.public_key,
                algorithms=[config.ALGORITHM],
                options={"verify_exp": True}
            )
        except ExpiredSignatureError as e:
            raise TokenExpiredError(message="Token expired") from e
        except InvalidTokenError as e:
            raise SignatureError(message="Token invalid") from e
