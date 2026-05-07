from pydantic import BaseModel


class UserFull(BaseModel):
    id: int
    email: str
    is_active: bool | None = False

class UserRegReq(BaseModel):
    email: str
    password: str

    model_config = {"extra": "forbid"}