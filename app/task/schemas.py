from pydantic import BaseModel, Field


class TaskFull(BaseModel):
    id: int
    project_id: int | None
    name: str
    description: str | None = None
    is_completed: bool = False

class TaskCreateReq(BaseModel):
    project_id: int
    name: str
    description: str | None = None

class TaskUpdateReq(BaseModel):
    project_id: int | None = None
    name: str | None = None
    description: str | None = None
    is_completed: bool = False

class TaskListParams(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(10, ge=1, le=100)
    q: str | None = None

class TaskListResp(BaseModel):
    items: list[TaskFull]
    total: int
    offset: int
    limit: int

