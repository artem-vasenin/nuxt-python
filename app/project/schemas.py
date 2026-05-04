from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator


class ProjectCreateReq(BaseModel):
    name: str
    description: str | None = None

    model_config = {"extra": "forbid"}

    @field_validator("name")
    @classmethod
    def key_not_empty(cls, value):
        if not value.strip():
            raise HTTPException(400, "name is empty")
        return value


class ProjectCreateResp(BaseModel):
    id: int
    name: str


class ProjectPath(BaseModel):
    pid: int = Field(gt=0)


class ProjectUpdateReq(BaseModel):
    name: str | None = None
    description: str | None = None


class ProductFullResp(BaseModel):
    id: int
    key: str
    name: str
    description: str | None
