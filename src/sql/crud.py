from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from sql.connect import async_session


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()