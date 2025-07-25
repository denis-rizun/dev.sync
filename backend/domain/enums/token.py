from enum import StrEnum


class JWTTokenType(StrEnum):
    ACCESS = 'access'
    REFRESH = 'refresh'
    DEV_TOKEN = 'dev_token'
