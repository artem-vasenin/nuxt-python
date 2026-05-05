from pydantic import BaseModel


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
