from pyrogram import Client, idle
from pyrogram.types import BotCommand
from pyrogram.enums import ParseMode

from _scheduler import scheduler
from _config import BOT_NAME, BOT_TOKEN, API_ID, API_HASH


bot = Client(
    BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="commands")
)


async def start_bot():
    await bot.start()
    scheduler.start()
    await bot.set_bot_commands([
        BotCommand("help", "顯示幫助"),
        BotCommand("leaderboard", "查看排行榜"),
        BotCommand("ping", "查看bot存活"),
        BotCommand("sign", "簽到"),
        BotCommand("title","自訂頭銜(消耗50積分)"),
        BotCommand("me","檢視自己的數據")
    ])
    print("Bot Started!")
    bot.set_parse_mode(ParseMode.MARKDOWN)
    await idle()