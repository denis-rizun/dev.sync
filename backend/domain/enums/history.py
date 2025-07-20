from enum import StrEnum


class HistoryTriggerEnum(StrEnum):
    MANUAL = "manual"
    SCHEDULED = "scheduled"
    AUTO = "auto"