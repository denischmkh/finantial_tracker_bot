import asyncio
from datetime import datetime
import pytz

from bot.bot import bot


def get_kiev_time():
    kiev_tz = pytz.timezone("Europe/Kiev")
    now_with_tz = datetime.now(kiev_tz)  # datetime с временной зоной
    return now_with_tz.replace(tzinfo=None)


async def delete_message(message_id: int,chat_id: int, time: int):
    await asyncio.sleep(time)
    await bot.delete_message(chat_id=chat_id, message_id=message_id)