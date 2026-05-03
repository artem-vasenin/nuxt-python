from fastapi import APIRouter, Request
import logging

from .schemas import Task, TaskCreateReq, TaskUpdateReq
from .services import TaskServiceDeps


router = APIRouter(prefix='/task', tags=['Tasks'])
logger = logging.getLogger(__name__)

@router.get('/', status_code=200, response_model=list[Task])
def get_list(serv: TaskServiceDeps, req: Request):
    logger.info('JWT %s', req.app.state.settings.auth.jwt, extra={'user_id': 34567})
    return serv.get_list()

@router.get('/{pid}', status_code=200, response_model=Task)
def get_item(pid: int, serv: TaskServiceDeps):
    logger.warning(f'ID: {pid}', extra={'user_id': 34567})
    return serv.get_item(pid)

@router.post('/', status_code=201, response_model=Task)
def set_item(data: TaskCreateReq, serv: TaskServiceDeps):
    return serv.set_item(data)

@router.patch('/{pid}')
def update_item(pid: int, data: TaskUpdateReq, serv: TaskServiceDeps):
    return serv.upd_item(pid, data)

@router.delete('/{pid}')
def delete_item(pid: int, serv: TaskServiceDeps):
    return serv.del_item(pid)
