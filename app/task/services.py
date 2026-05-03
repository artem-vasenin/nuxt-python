from typing import Annotated
from fastapi import Depends

from .schemas import TaskCreateReq, Task, TaskUpdateReq
from .repos import TaskRepo, TaskRepoDeps


class TaskService():
    def __init__(self, repo: TaskRepo):
        self.repo = repo

    def get_list(self) -> list[Task]:
        return self.repo.get_list()

    def get_item(self, pid: int) -> Task:
        return self.repo.get_item(pid)

    def set_item(self, data: TaskCreateReq) -> Task:
        return self.repo.set_item(data)

    def upd_item(self, pid: int, data: TaskUpdateReq) -> Task:
        return self.repo.upd_item(pid, data)

    def del_item(self, pid: int) -> bool:
        return self.repo.del_item(pid)


def get_task_service(repo: TaskRepoDeps):
    return TaskService(repo)

TaskServiceDeps = Annotated[
    TaskService,
    Depends(get_task_service)
]
