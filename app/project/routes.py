from fastapi import APIRouter, Depends
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
def add_project(data: ProjectCreateReq, service: ProjServiceDeps)->ProductFullResp:
    return service.set_project(data)

@router.get(
    "",
    response_model=list[ProductFullResp],
    summary='Get all Projects'
)
def get_projects(service: ProjServiceDeps):
    return service.get_projects()

@router.get(
    "/{pid}",
    response_model=ProductFullResp | None,
    summary='Get Project by id'
)
def get_project(service: ProjServiceDeps, path: ProjectPath = Depends()):
    return service.get_project(path.pid)

@router.patch(
    "/{pid}",
    response_model=ProductFullResp,
    status_code=201,
    summary='Update Project'
)
def update_project(data: ProjectUpdateReq, path: ProjectPath = Depends()):
    return ProductFullResp(
        id=path.pid,
        key="123",
        name=data.name,
        description=data.description,
    )

@router.delete(
    "/{pid}",
    response_model=bool,
    summary='Get Project by id'
)
def del_project(service: ProjServiceDeps, path: ProjectPath = Depends()):
    return service.del_project(path.pid)
