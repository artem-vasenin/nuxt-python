from sqlalchemy import String, Text, Boolean, Any
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class TaskModel(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)

    def __init__(self, name: str, description: str | None = None, is_completed: bool = False, **kw: Any):
        super().__init__(**kw)
        self.name = name
        self.description = description
        self.is_completed = is_completed
