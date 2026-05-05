from pydantic import BaseModel


class TaskFull(BaseModel):
    id: int
    # proj_id: int
    name: str
    description: str | None = None
    is_completed: bool = False

class TaskCreateReq(BaseModel):
    # proj_id: int
    name: str
    description: str | None = None

class TaskUpdateReq(BaseModel):
    # proj_id: int | None = None
    name: str | None = None
    description: str | None = None
    is_completed: bool = False
