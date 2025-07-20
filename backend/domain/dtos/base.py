from dataclasses import dataclass, fields
from typing import Any

from backend.domain.enums.common import ColumnEnum


@dataclass
class BaseUpdateDTO:
    def to_raw(self) -> dict[ColumnEnum, Any]:
        raw = {}
        for f in fields(self):
            value = getattr(self, f.name)
            if value is not None:
                enum_key_name = f.name.upper()
                try:
                    column_enum_key = getattr(ColumnEnum, enum_key_name)
                except AttributeError:
                    continue

                raw[column_enum_key] = value
        return raw
