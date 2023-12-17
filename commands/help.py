from pyrogram import Client, filters

from _config import BOT_NAME, INFO_DELETE_TIME
from _utils import reply_and_delay_delete

HELP_MESSAGE = f"""
```
/help@{BOT_NAME}               顯示幫助訊息
/ping@{BOT_NAME}               查看只因器人活著嗎
/leaderboard@{BOT_NAME}        查看排行榜
/sign@{BOT_NAME}               簽到
/title@{BOT_NAME}              自訂頭銜(消耗50積分)
/me@{BOT_NAME}                 檢視自己的數據
```

感謝您的使用
v0.0.1 PlanTech
"""


@Client.on_message(filters.command('help'), group=0)
async def help_message(_, message):
    await reply_and_delay_delete(message, HELP_MESSAGE, INFO_DELETE_TIME)