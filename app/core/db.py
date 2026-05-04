from typing import AsyncGenerator, Annotated
from fastapi import Depends

from app.core.settings import Settings
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)


settings = Settings() # type: ignore[call-arg]
engine = create_async_engine(
    settings.db_url,
    echo=False,
    pool_pre_ping=True,
)
session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with session() as s:
        yield s

async def check(session: AsyncSession):
    res = await session.execute(select(1))
    return res.scalar_one()

DbSessionDeps = Annotated[
    AsyncSession,
    Depends(get_session),
]

class Base(DeclarativeBase):
    ...