from fastapi import APIRouter, Depends
from .schema import (
    ProjectCreateReq,
    ProjectCreateResp,
    ProjectPath,
    ProjectUpdateReq,
    ProductFullResp,
)
from .services import ProjServiceDeps


router = APIRouter(prefix="/project", tags=['Projects'])


@router.post(
    "",
    response_model=ProjectCreateResp,
    status_code=201,
    summary='Add new Project',
    description='''
    Do you want add new Project?\n
    The Project is main item of Jira\n
    Projects is parents for Tasks
    '''
)
def add_project(data: ProjectCreateReq, service: ProjServiceDeps):
    return ProjectCreateResp(id=service.get_project(17), name=data.name)


@router.get(
    "/{pid}",
    response_model=ProductFullResp,
    summary='Get Project by id'
)
def get_project(path: ProjectPath = Depends()):
    return ProductFullResp(id=path.pid, name="some", key="Some_key", description=None)


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
