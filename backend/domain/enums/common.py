from enum import StrEnum


class ServerStatusEnum(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class StatusEnum(StrEnum):
    SUCCESS = "success"
    IN_PROGRESS = "in_progress"
    ERROR = "error"
    WAITING = "waiting"
    EXCEPT = "except"


class ColumnEnum(StrEnum):
    ID = "id"
    USERNAME = "username"
    REVOKED = "revoked"
    USER_ID = "user_id"
    SERVER_STATUS = "server_status"
    STATUS = "status"
