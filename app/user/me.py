from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.user.schemes import UserFull
from app.user.security import check_token
from app.user.services import UserServiceDeps


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def me(token: Annotated[str, Depends(oauth2_scheme)], u_service: UserServiceDeps)->UserFull:
    uid = check_token(token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await u_service.get_item_by_id(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

MeDeps = Annotated[UserFull, Depends(me)]