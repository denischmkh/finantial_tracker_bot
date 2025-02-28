
import logging
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config import DATABASE_URL

DATABASE_URL = DATABASE_URL.split('://')
DATABASE_URL[0] += '+asyncpg'
DATABASE_URL = "://".join(DATABASE_URL)



DATABASE_URL_WITH_ASYNC_ENGINE = DATABASE_URL

engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s [%(asctime)s]: %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8')


async def init_db_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        logging.info('База данных удалена')
        await conn.run_sync(Base.metadata.create_all)
        logging.info('База данных создана')


