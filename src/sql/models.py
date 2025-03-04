import uuid

from bot.utils import get_kiev_time
from sql.connect import Base
from sqlalchemy import DATETIME, Integer, String, DECIMAL, UUID, Column, ForeignKey, TIMESTAMP


class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID, primary_key=True, unique=True, default=uuid.uuid4)


class User(BaseModel):
    __tablename__ = "users"
    user_id = Column(Integer, unique=True, nullable=False)


class ProductExpenses(BaseModel):
    __tablename__ = "product_expenses"
    summa = Column(DECIMAL(10, 2), nullable=False)
    created = Column(TIMESTAMP(timezone=False), default=get_kiev_time)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)


class OtherExpenses(BaseModel):
    __tablename__ = "other_expenses"
    summa = Column(DECIMAL(10, 2), nullable=False)
    created = Column(TIMESTAMP(timezone=False), default=get_kiev_time)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)


class TransportExpenses(BaseModel):
    __tablename__ = "transport_expenses"
    summa = Column(DECIMAL(10, 2), nullable=False)
    created = Column(TIMESTAMP(timezone=False), default=get_kiev_time)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)


class EveryMonthExpenses(BaseModel):
    __tablename__ = 'every_month_expenses'
    title = Column(String, nullable=False)
    summa = Column(DECIMAL(10, 2), nullable=False)
    created = Column(TIMESTAMP(timezone=False), default=get_kiev_time)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)


class Earnings(BaseModel):
    __tablename__ = 'earnings'
    summa = Column(DECIMAL(10, 2), nullable=False)
    created = Column(TIMESTAMP(timezone=False), default=get_kiev_time)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
