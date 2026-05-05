from typing import Annotated
from fastapi import Depends, HTTPException

from .models import TaskModel
from .schemas import TaskCreateReq, TaskFull, TaskUpdateReq
from .repos import TaskRepo, TaskRepoDeps


def transform_task(item: TaskModel)->TaskFull:
    return TaskFull(
        id=item.id,
        name=item.name,
        description=item.description,
        is_completed=item.is_completed,
        project_id=item.project_id,
    )

class TaskService:
    def __init__(self, repo: TaskRepo):
        self.repo = repo

    async def get_list(self) -> list[TaskModel]:
        return await self.repo.get_list()

    async def get_item(self, pid: int) -> TaskFull:
        result = await self.repo.get_item(pid)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return transform_task(result)

    async def set_item(self, data: TaskCreateReq) -> TaskFull:
        result = await self.repo.set_item(data)
        return transform_task(result)

    async def upd_item(self, pid: int, data: TaskUpdateReq) -> TaskFull:
        result = await self.repo.upd_item(pid, data)
        return transform_task(result)

    async def del_item(self, pid: int) -> bool:
        return await self.repo.del_item(pid)


def get_task_service(repo: TaskRepoDeps):
    return TaskService(repo)

TaskServiceDeps = Annotated[
    TaskService,
    Depends(get_task_service)
]
