from typing import Annotated
from fastapi import Depends, HTTPException

from app.user.schemes import UserFull
from .models import ProjectModel
from .repos import ProjectRepo, ProjectRepoDeps
from .schemas import ProjectCreateReq, ProductFullResp, ProjectUpdateReq


class ProjectService():
    def __init__(self, repo: ProjectRepo):
        self.repo = repo

    async def get_projects(self) -> list[ProductFullResp]:
        return await self.repo.get_list()

    async def get_project(self, pid: int, uid: int)->ProductFullResp:
        res = await self.repo.get_by_id(pid)
        if not res:
            raise HTTPException(status_code=404, detail="Project not found")
        perm = await self.repo.get_project_permission(pid, uid)
        if not perm:
            raise HTTPException(status_code=404, detail="Project not found")
        return ProductFullResp(id=res.id, key=res.key, name=res.name, description=res.description)

    async def set_project(self, data: ProjectCreateReq, user: UserFull)->ProductFullResp:
        item = ProjectModel(**data.model_dump())
        result = await self.repo.set_item(item, user)
        return ProductFullResp(id=result.id, key=result.key, name=result.name, description=result.description)

    async def update_project(self, pid: int, data: ProjectUpdateReq)->ProductFullResp:
        result = await self.repo.update_item(pid, data)
        return ProductFullResp(id=result.id, key=result.key, name=result.name, description=result.description)

    async def del_project(self, pid: int)->bool:
        return await self.repo.del_item(pid)

def get_pr_serv(repo: ProjectRepoDeps):
    return ProjectService(repo)

ProjServiceDeps = Annotated[
    ProjectService,
    Depends(get_pr_serv)
]
