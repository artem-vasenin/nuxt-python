import logging
from typing import Annotated
from sqlalchemy import select, func, or_
from fastapi import Depends, HTTPException

from .models import TaskModel
from app.project.models import ProjectModel
from .schemas import TaskCreateReq, TaskUpdateReq
from app.core.db import DbSessionDeps, AsyncSession


logger = logging.getLogger(__name__)

class TaskRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self, offset: int = 0, limit: int = 10, q: str = None) -> tuple[list[TaskModel], int]:
        cnt_query = select(func.count()).select_from(TaskModel)
        list_query = select(TaskModel)

        if q and q.strip():
            cnt_query = cnt_query.where(
                or_(TaskModel.name.ilike(f"%{q}%"), TaskModel.description.ilike(f"%{q}%"))
            )
            list_query = list_query.where(
                or_(TaskModel.name.ilike(f"%{q}%"), TaskModel.description.ilike(f"%{q}%"))
            )

        total = (await self.session.execute(cnt_query)).scalar_one()
        list_query.order_by(TaskModel.id).offset(offset).limit(limit)
        items = list((await self.session.execute(list_query)).scalars().all())
        return items, total

    async def get_item(self, pid: int) -> TaskModel | None:
        return await self.session.get(TaskModel, pid)

    async def set_item(self, data: TaskCreateReq) -> TaskModel:
        if not data.project_id:
            raise HTTPException(status_code=400, detail="Project id is required")
        project = await self.session.get(ProjectModel, data.project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        item = TaskModel(**data.model_dump())
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def upd_item(self, pid: int, data: TaskUpdateReq) -> TaskModel:
        item = await self.get_item(pid)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        if data.project_id:
            project = await self.session.get(ProjectModel, data.project_id)
            if not project:
                raise HTTPException(status_code=404, detail="Project not found")
        patch = data.model_dump(exclude_unset=True)
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
