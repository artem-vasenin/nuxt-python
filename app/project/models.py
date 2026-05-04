import time
from sqlalchemy import String, Text, Any

from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class ProjectModel(Base):
    __tablename__ = 'project'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(String(128), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)

    def __init__(self, name: str, description: str | None = None, **kw: Any):
        super().__init__(**kw)
        self.key = str(time.time())
        self.name = name
        self.description = description
