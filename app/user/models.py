from typing import Any, TYPE_CHECKING
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from app.project.models import ProjectUserModel

class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    project_user: Mapped[list['ProjectUserModel']] = relationship(
        'ProjectUserModel', back_populates='user'
    )

    def __init__(self, email: str, password: str, is_active: bool = True, **kwargs: Any):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.is_active = is_active