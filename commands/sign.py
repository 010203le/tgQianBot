from _utils import reply_and_delay_delete
from _config import INFO_DELETE_TIME, MODE, CHAT_ID

from pyrogram import Client, filters

import random

if MODE == 'MS_SQL':
    import _sqlexec_MS as _q
elif MODE == 'MySQL':
    import _sqlexec as _q
else:
    raise ValueError

@Client.on_message(filters.command('sign'), group=0)
async def sign_message(_, message):
    luck = random.randint(1,20)
    user_id = message.from_user.id
    #print(message.chat.id)
    if message.chat.id != CHAT_ID:
        await reply_and_delay_delete(message,  '僅在指定群組可用。', INFO_DELETE_TIME)
    else:
        qian = _q.q(user_id,luck)
        await reply_and_delay_delete(message,  '['+str(user_id)+'](tg://user?id='+str(user_id)+') 你好，'+qian, INFO_DELETE_TIME)