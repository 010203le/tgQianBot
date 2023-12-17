from _utils import reply_and_delay_delete
from _config import INFO_DELETE_TIME, MODE, CHAT_ID

from pyrogram import Client, filters

if MODE == 'MS_SQL':
    import _sqlexec_MS as _lb
elif MODE == 'MySQL':
    import _sqlexec as _lb
else:
    raise ValueError

@Client.on_message(filters.command('leaderboard'), group=0)
async def leaderboard_message(_, message):
    lb = _lb.lb()
    await reply_and_delay_delete(message, lb, INFO_DELETE_TIME)