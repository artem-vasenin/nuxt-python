from fastapi import APIRouter, Depends

from app.user.me import MeDeps
from .schemas import (
    ProjectCreateReq,
    ProjectPath,
    ProjectUpdateReq,
    ProductFullResp,
)
from .services import ProjServiceDeps


router = APIRouter(prefix="/project", tags=['Projects'])

@router.post(
    "",
    response_model=ProductFullResp,
    status_code=201,
    summary='Add new Project',
    description='''
    Do you want add new Project?\n
    The Project is main item of Jira\n
    Projects is parents for Tasks
    '''
)
async def add_project(data: ProjectCreateReq, service: ProjServiceDeps, user: MeDeps)->ProductFullResp:
    return await service.set_project(data, user)

@router.get(
    "",
    response_model=list[ProductFullResp],
    summary='Get all Projects'
)
async def get_projects(service: ProjServiceDeps):
    return await service.get_projects()

@router.get(
    "/{pid}",
    response_model=ProductFullResp | None,
    summary='Get Project by id'
)
async def get_project(service: ProjServiceDeps, me: MeDeps, path: ProjectPath = Depends()):
    return await service.get_project(path.pid, me.id)

@router.patch(
    "/{pid}",
    response_model=ProductFullResp,
    status_code=201,
    summary='Update Project'
)
async def update_project(service: ProjServiceDeps, data: ProjectUpdateReq, path: ProjectPath = Depends()):
    return await service.update_project(path.pid, data)

@router.delete(
    "/{pid}",
    status_code=201,
    response_model=bool,
    summary='Get Project by id'
)
async def del_project(service: ProjServiceDeps, path: ProjectPath = Depends()):
    return await service.del_project(path.pid)
