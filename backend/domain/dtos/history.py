from dataclasses import dataclass

from backend.domain.dtos.base import BaseUpdateDTO
from backend.domain.enums.common import StatusEnum


@dataclass
class HistoryUpdateDTO(BaseUpdateDTO):
    status: StatusEnum | None = None
