from _utils import reply_and_delay_delete
from _config import INFO_DELETE_TIME, MODE,CHAT_ID

from pyrogram import Client, filters

if MODE == 'MS_SQL':
    import _sqlexec_MS as _me
elif MODE == 'MySQL':
    import _sqlexec as _me
else:
    raise ValueError

@Client.on_message(filters.command('me'), group=0)
async def me_message(_, message):
    user_id = message.from_user.id
    if message.chat.id != CHAT_ID:
        await reply_and_delay_delete(message,  '僅在指定群組可用。', INFO_DELETE_TIME)
    else:
        me = _me.me(user_id)
        await reply_and_delay_delete(message, '['+str(user_id)+'](tg://user?id='+str(user_id)+') 的數據如下\n'+me, INFO_DELETE_TIME)