from typing import Annotated
from fastapi import HTTPException, Depends

from app.user.repos import UserRepo, UserRepoDeps
from app.user.schemes import UserFull, UserRegReq


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    async def get_item(self, email: str)->UserFull:
        res = await self.repo.get_item(email)
        if not res:
            raise HTTPException(status_code=404, detail="Item not found")
        return UserFull(id=res.id, email=res.email, is_active=res.is_active)

    async def set_item(self, data: UserRegReq)->str:
        res = await self.repo.set_item(data)
        if not res:
            raise HTTPException(status_code=404, detail="Item not found")
        return res

    async def login(self, data: UserRegReq)->str:
        res = await self.repo.login(data)
        if not res:
            raise HTTPException(status_code=404, detail="User not found")
        return res

    async def del_item(self, pid: int)->bool:
        return await self.repo.del_item(pid)

def get_service(repo: UserRepoDeps):
    return UserService(repo)

UserServiceDeps = Annotated[
    UserService,
    Depends(get_service)
]