import logging
from typing import Annotated
from fastapi import Depends
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

    async def update_item(self, pid: int, data: ProjectUpdateReq) -> ProductFullResp | None:
        return None

    def del_item(self, pid: int) -> bool:
        flag = False
        return flag


def get_project_repo(session: DbSessionDeps):
    return ProjectRepo(session)

ProjectRepoDeps = Annotated[
    ProjectRepo,
    Depends(get_project_repo),
]
