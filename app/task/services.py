from typing import Annotated
from fastapi import Depends, HTTPException

from .models import TaskModel
from .schemas import TaskCreateReq, TaskFull, TaskUpdateReq, TaskListParams, TaskListResp
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

    async def get_list(self, params: TaskListParams) -> TaskListResp:
        lst, total = await self.repo.get_list(offset=params.offset, limit=params.limit, q=params.q)
        return TaskListResp(
            items=[TaskFull(
                id=i.id,
                name=i.name,
                description=i.description,
                is_completed=i.is_completed,
                project_id=i.project_id,
            ) for i in lst],
            total=total,
            offset=params.offset,
            limit=params.limit,
        )

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
