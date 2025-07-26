from dataclasses import asdict
from typing import Generic

from backend.domain.types import EntityType, ModelType


class BaseMapper(Generic[EntityType, ModelType]):
    ENTITY: type[EntityType]
    MODEL: type[ModelType]

    @classmethod
    def to_entity(cls, model: ModelType) -> EntityType:
        data = {k: getattr(model, k) for k in model.__dict__ if not k.startswith('_')}
        return cls.ENTITY(**data)

    @classmethod
    def to_model(cls, entity: EntityType) -> ModelType:
        data = asdict(entity)
        return cls.MODEL(**data)
