from typing import AsyncGenerator
from app.core.settings import Settings
from sqlalchemy import text
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

async def check():
    async with engine.connect() as c:
        res = await c.execute(text('select 1'))
        return res.scalar_one()
