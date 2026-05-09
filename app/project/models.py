import time
from typing import TYPE_CHECKING
from sqlalchemy import String, Text, Any, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from app.task.models import TaskModel
    from app.user.models import UserModel

class ProjectModel(Base):
    __tablename__ = 'project'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(String(128), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
    tasks: Mapped[list["TaskModel"]] = relationship(
        "TaskModel",
        back_populates="project",
        cascade="all, delete-orphan",
    )
    project_user: Mapped[list['ProjectUserModel']] = relationship(
        'ProjectUserModel', back_populates='project'
    )

    def __init__(self, name: str, description: str | None = None, **kw: Any):
        super().__init__(**kw)
        self.key = str(time.time())
        self.name = name
        self.description = description

class ProjectUserModel(Base):
    __tablename__ = 'project_user'

    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", onupdate="CASCADE", ondelete="CASCADE",
    ), primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey(
        "project.id", onupdate="CASCADE", ondelete="CASCADE",
    ), primary_key=True)
    user: Mapped['UserModel'] = relationship('UserModel', back_populates="project_user")
    project: Mapped['ProjectModel'] = relationship('ProjectModel', back_populates="project_user")
    role: Mapped[str] = mapped_column(String(50), default='member')

    def __init__(self, user_id: int, project_id: int, role: str, **kw: Any):
        super().__init__(**kw)
        self.user_id = user_id
        self.project_id = project_id
        self.role = role
