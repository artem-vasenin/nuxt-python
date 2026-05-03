from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    pid: int
    proj_id: int
    name: str
    description: str | None = None
    created_at: datetime
    deadline: datetime

class TaskCreateReq(BaseModel):
    proj_id: int
    name: str
    description: str | None = None
    deadline: datetime

class TaskUpdateReq(BaseModel):
    proj_id: int | None = None
    name: str | None = None
    description: str | None = None
    deadline: datetime | None = None
