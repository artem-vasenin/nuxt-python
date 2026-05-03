from typing import Annotated
from fastapi import Depends

from .schemas import ProjectCreateReq, ProductFullResp

from .repos import ProjectRepo, ProjectRepoDeps


class ProjectService():
    def __init__(self, repo: ProjectRepo):
        self.repo = repo

    def get_projects(self) -> list[ProductFullResp]:
        return self.repo.get_list()

    def get_project(self, pid: int):
        return self.repo.get_by_id(pid)

    def set_project(self, data: ProjectCreateReq):
        return self.repo.set_item(data)

    def del_project(self, pid: int):
        return self.repo.del_item(pid)

def get_pr_serv(repo: ProjectRepoDeps):
    return ProjectService(repo)

ProjServiceDeps = Annotated[
    ProjectService,
    Depends(get_pr_serv)
]
