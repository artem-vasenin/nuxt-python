from typing import Annotated

from fastapi import Depends


class ProjectRepo():
    def get_by_id(self, pid: int):
        return pid

def get_project_repo():
    return ProjectRepo()

ProjectRepoDeps = Annotated[
    ProjectRepo,
    Depends(get_project_repo),
]
