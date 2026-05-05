import logging
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy import select

from app.core.db import DbSessionDeps, AsyncSession
from .schemas import ProductFullResp, ProjectUpdateReq
from .models import ProjectModel


logger = logging.getLogger(__name__)

class ProjectRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_list(self) -> list[ProjectModel]:
        result = await self.session.execute(select(ProjectModel))
        return result.scalars().all()

    async def get_by_id(self, pid: int) -> type[ProjectModel] | None:
        return await self.session.get(ProjectModel, pid)

    async def set_item(self, item: ProjectModel) -> ProjectModel:
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        logger.info(f'Project {item.key} created')

        return item

    async def update_item(self, pid: int, data: ProjectUpdateReq) -> ProjectModel:
        item = await self.get_by_id(pid)
        if not item:
            raise HTTPException(status_code=404, detail='Project not found')
        patch = data.model_dump(exclude_unset=True)
        for f, v in patch.items():
            setattr(item, f, v)
        await self.session.commit()
        await self.session.refresh(item)

        return item

    async def del_item(self, pid: int) -> bool:
        item = await self.get_by_id(pid)
        if not item:
            return False
        await self.session.delete(item)
        await self.session.commit()
        return True


def get_project_repo(session: DbSessionDeps):
    return ProjectRepo(session)

ProjectRepoDeps = Annotated[
    ProjectRepo,
    Depends(get_project_repo),
]
