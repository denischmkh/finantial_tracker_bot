from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from sql.connect import async_session

import sqlalchemy as _sql

from sql.models import User, ProductExpenses


@asynccontextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()


class UserCRUD:
    @staticmethod
    async def create_new_user(user_id) -> None:
        async with get_session() as session:
            try:
                user_model = User(user_id=user_id)
                session.add(user_model)
                await session.commit()
            except:
                pass


class ProductCrud:
    @staticmethod
    async def create_expense(summa: float, user_id: int) -> bool:
        async with get_session() as session:
            try:
                expense_model = ProductExpenses(summa=summa, user_id=user_id)
                session.add(expense_model)
                await session.commit()
                return True
            except Exception as e:
                print(e)
                await session.rollback()
                return False
