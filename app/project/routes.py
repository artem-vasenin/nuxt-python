from fastapi import APIRouter, Depends
from .schema import ProjectCreateReq, ProjectCreateResp, ProjectPath, ProjectUpdateReq, ProductFullResp


router = APIRouter(prefix='/project')

@router.post('', response_model=ProjectCreateResp)
def add_project(data: ProjectCreateReq):
    return ProjectCreateResp(id=1, name=data.name)

@router.get('/{pid}')
def get_project(pid: ProjectPath = Depends()):
    return pid

@router.patch('/{pid}', response_model=ProductFullResp)
def update_project(data: ProjectUpdateReq, path: ProjectPath = Depends()):
    return ProductFullResp(
        id=path.pid,
        key='123',
        name=data.name,
        description=data.description,
    )
