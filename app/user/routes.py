from fastapi import APIRouter

from app.user.schemes import UserFull, UserRegReq
from app.user.services import UserServiceDeps


router = APIRouter(prefix='/auth', tags=['Auth'])

@router.get('/{email}', status_code=200, response_model=UserFull)
async def get_item(email: str, serv: UserServiceDeps)->UserFull:
    return await serv.get_item(email)

@router.post('/', status_code=201, response_model=str)
async def set_item(data: UserRegReq, serv: UserServiceDeps)->str:
    return await serv.set_item(data)

@router.post('/login', status_code=200, response_model=str)
async def login(data: UserRegReq, serv: UserServiceDeps)->str:
    return await serv.login(data)

@router.delete('/{pid}', status_code=201, response_model=bool)
async def delete_item(pid: int, serv: UserServiceDeps)->bool:
    return await serv.del_item(pid)