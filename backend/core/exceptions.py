class DevSyncError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

# ----------------- DATABASE -----------------
class DatabaseError(DevSyncError):
    pass


class NotFoundError(DatabaseError):
    pass


class DuplicateDataError(DatabaseError):
    pass

# ----------------- Validation -----------------
class ValidationError(DevSyncError):
    pass
