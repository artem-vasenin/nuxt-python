from datetime import datetime
from typing import Annotated

from fastapi import Depends, HTTPException
from .schemas import Task, TaskCreateReq, TaskUpdateReq


tasks = [
    Task(
        pid=1,
        proj_id=1,
        name='Task 1',
        description='The task one',
        created_at=datetime.now(),
        deadline=datetime.now(),
    ),
    Task(
        pid=2,
        proj_id=5,
        name='Task 2',
        description='The task two',
        created_at=datetime.now(),
        deadline=datetime.now(),
    ),
    Task(
        pid=3,
        proj_id=3,
        name='Task 3',
        description='The task three',
        created_at=datetime.now(),
        deadline=datetime.now(),
    ),
]

class TaskRepo():
    def get_list(self) -> list[Task]:
        return tasks

    def get_item(self, pid: int) -> Task:
        res = list(filter(lambda x: x.pid == pid, tasks))
        if not len(res):
            raise HTTPException(404, "Item is not found")
        return res[0]

    def set_item(self, data: TaskCreateReq) -> Task:
        max_id = 0
        for i in tasks:
            if i.pid > max_id:
                max_id = i.pid
        candidate = Task(
            pid=(max_id + 1),
            proj_id=data.proj_id,
            name=data.name,
            description=data.description if data.description else None,
            created_at=datetime.now(),
            deadline=data.deadline,
        )
        tasks.append(candidate)
        return self.get_item(max_id + 1)

    def upd_item(self, pid: int, data: TaskUpdateReq) -> Task:
        for i in tasks:
            if i.pid == pid:
                i.proj_id = data.proj_id if data.proj_id else i.proj_id
                i.name = data.name if data.name else i.name
                i.description = data.description if data.description else i.description
                i.deadline = data.deadline if data.deadline else i.deadline
        return self.get_item(pid)

    def del_item(self, pid: int) -> bool:
        for idx, item in enumerate(tasks):
            if item.pid == pid:
                del tasks[idx]
                return True
        return False

def get_task_repo():
    return TaskRepo()

TaskRepoDeps = Annotated[
    TaskRepo,
    Depends(get_task_repo)
]
