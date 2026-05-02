from typing import Annotated
from fastapi import Depends

from app.project.repos import ProjectRepo, ProjectRepoDeps


class ProjectService():
    def __init__(self, repo: ProjectRepo):
        self.repo = repo

    def get_project(self, pid: int):
        return self.repo.get_by_id(pid)

def get_pr_serv(repo: ProjectRepoDeps):
    return ProjectService(repo)

ProjServiceDeps = Annotated[
    ProjectService,
    Depends(get_pr_serv)
]
