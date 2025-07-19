from pydantic import BaseModel


class DevSyncSchema(BaseModel):

    class Config:
        from_attributes = True
