import logging
from typing import Annotated
from sqlalchemy import select
from fastapi import Depends, HTTPException

from .models import TaskModel
from .schemas import TaskCreateReq, TaskUpdateReq
from app.core.db import DbSessionDeps, AsyncSession


logger = logging.getLogger(__name__)

class TaskRepo():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self) -> list[TaskModel]:
        items = await self.session.execute(select(TaskModel))
        return items.scalars().all()

    async def get_item(self, pid: int) -> type[TaskModel] | None:
        return await self.session.get(TaskModel, pid)

    async def set_item(self, data: TaskCreateReq) -> TaskModel:
        item = TaskModel(**data.model_dump())
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def upd_item(self, pid: int, data: TaskUpdateReq) -> TaskModel:
        item = await self.get_item(pid)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        patch = data.model_dump(exclude_unset=True)
        print(patch)
        for f, v in patch.items():
            setattr(item, f, v)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def del_item(self, pid: int) -> bool:
        item = await self.get_item(pid)
        if not item:
            return False
        await self.session.delete(item)
        await self.session.commit()
        return True

def get_task_repo(session: DbSessionDeps):
    return TaskRepo(session)

TaskRepoDeps = Annotated[
    TaskRepo,
    Depends(get_task_repo)
]
