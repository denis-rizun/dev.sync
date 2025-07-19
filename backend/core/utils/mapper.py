from dataclasses import asdict
from typing import Generic

from backend.domain.types import SchemaType, DTOType, EntityType


class Mapper(Generic[SchemaType, DTOType, EntityType]):
    @staticmethod
    def to_dto(dto: DTOType, schema: SchemaType) -> DTOType:
        return dto(**schema.model_dump())

    @staticmethod
    def to_schema(schema: SchemaType, dto: DTOType) -> SchemaType:
        return schema(**asdict(dto))

    @staticmethod
    def to_entity(entity: EntityType, dto: DTOType) -> EntityType:
        return entity(**asdict(dto))
