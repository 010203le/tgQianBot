import contextlib
import datetime

import pytz

from pyrogram.types import Message
from _scheduler import scheduler
from _config import TIME_ZONE

async def _delete_message(message) -> bool:
    with contextlib.suppress(Exception):
        await message.delete()
        return True
    return False

def add_delete_message_job(message: Message, time: int) -> None:
    scheduler.add_job(
        _delete_message,
        "date",
        id=f"{message.chat.id}|{message.id}|delete_message",
        name=f"{message.chat.id}|{message.id}|delete_message",
        args=[message],
        run_date=datetime.datetime.now(pytz.timezone(TIME_ZONE)) + datetime.timedelta(seconds=time),
        replace_existing=True,
    )


async def delay_delete(message: Message, time: int = 10) -> None:
    add_delete_message_job(message, time)


async def edit_and_delay_delete(message: Message, text: str, time: int = 10) -> None:
    await message.edit(text)
    add_delete_message_job(message, time)


async def reply_and_delay_delete(message: Message, text: str, time: int = 10) -> None:
    message = await message.reply(text)
    add_delete_message_job(message, time)
