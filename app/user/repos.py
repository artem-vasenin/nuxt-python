import logging
from typing import Annotated
from sqlalchemy import select
from fastapi import HTTPException, Depends

from app.user.models import UserModel
from app.user.schemes import UserRegReq
from app.user.security import hash_password, verify_password, add_token, check_token
from app.core.db import DbSessionDeps, AsyncSession


logger = logging.getLogger(__name__)

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_item(self, email: str) -> type[UserModel] | None:
        return (await self.session.execute(
            select(UserModel).where(UserModel.email == email)
        )).scalar_one_or_none()

    async def get_item_by_id(self, pid: int) -> type[UserModel] | None:
        return await self.session.get(UserModel, pid)

    async def set_item(self, data: UserRegReq) -> str:
        double_item = await self.get_item(data.email)
        if double_item:
            logger.error(f"{data.email} already registered")
            raise HTTPException(status_code=400, detail="Email already registered")

        try:
            hashed = hash_password(data.password)
        except Exception as exc:
            logger.error(exc)
            raise HTTPException(status_code=400, detail=str(exc))

        item = UserModel(email=data.email, password=hashed)
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return add_token(item.id)

    async def login(self, data: UserRegReq) -> str | None:
        item = await self.get_item(data.email)
        if not item:
            raise HTTPException(status_code=404, detail="User is not found")
        if not verify_password(data.password, item.password):
            raise HTTPException(status_code=400, detail="User is not found")
        return add_token(item.id)

    async def del_item(self, pid: int) -> bool:
        item = await self.session.get(UserModel, pid)
        if not item:
            return False
        await self.session.delete(item)
        await self.session.commit()
        return True

def get_repo(session: DbSessionDeps):
    return UserRepo(session)

UserRepoDeps = Annotated[
    UserRepo,
    Depends(get_repo)
]