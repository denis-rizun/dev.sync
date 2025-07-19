from enum import StrEnum


class JWTTokenType(StrEnum):
    ACCESS = 'access'
    REFRESH = 'refresh'
