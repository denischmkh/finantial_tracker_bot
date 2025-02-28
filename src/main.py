import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.types import Message, URLInputFile

from bot.expenses_routers.earnings_router import router as earnings_router
from bot.expenses_routers.transport_router import router as transport_expenses_router
from bot.expenses_routers.other_router import router as other_expenses_router
from bot.expenses_routers.product_router import router as product_expenses_router
from bot.expenses_routers.every_month_router import router as every_month_expenses_router


from bot.keyboards import start_markup
from config import BOT_TOKEN

redis = Redis(host="localhost")

storage = RedisStorage(redis=redis)

bot = Bot(BOT_TOKEN)
dp = Dispatcher(storage=storage)


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer_photo(
        photo=URLInputFile(url='https://images.dwncdn.net/images/t_app-icon-l/p/70516662-7863-11e8-b063-02420a000b02/415023659/2057_4-76281062-logo'),
        caption='Добро пожаловать в финансовый трекер\nВыбери интересующую категорию',
        reply_markup=start_markup()
    )
    await message.delete()


async def main():
    dp.include_router(transport_expenses_router)
    dp.include_router(other_expenses_router)
    dp.include_router(product_expenses_router)
    dp.include_router(every_month_expenses_router)
    dp.include_router(earnings_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())