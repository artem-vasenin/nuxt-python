from fastapi import APIRouter

from .services import TaskServiceDeps
from .schemas import TaskFull, TaskCreateReq, TaskUpdateReq


router = APIRouter(prefix='/task', tags=['Tasks'])

@router.get('/', status_code=200, response_model=list[TaskFull])
async def get_list(serv: TaskServiceDeps)->list[TaskFull]:
    return await serv.get_list()

@router.get('/{pid}', status_code=200, response_model=TaskFull)
async def get_item(pid: int, serv: TaskServiceDeps)->TaskFull:
    return await serv.get_item(pid)

@router.post('/', status_code=201, response_model=TaskFull)
async def set_item(data: TaskCreateReq, serv: TaskServiceDeps)->TaskFull:
    return await serv.set_item(data)

@router.patch('/{pid}', status_code=201, response_model=TaskFull)
async def update_item(pid: int, data: TaskUpdateReq, serv: TaskServiceDeps)->TaskFull:
    return await serv.upd_item(pid, data)

@router.delete('/{pid}', status_code=201, response_model=bool)
async def delete_item(pid: int, serv: TaskServiceDeps)->bool:
    return await serv.del_item(pid)
