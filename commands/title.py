from _utils import reply_and_delay_delete
from _config import INFO_DELETE_TIME, MODE

from pyrogram import Client, filters


if MODE == 'MS_SQL':
    import _sqlexec_MS as _title
elif MODE == 'MySQL':
    import _sqlexec as _title
else:
    raise ValueError

black_list = ['管理員', 'admin', 'owner', '擁有者', '所有者', '管理员']

@Client.on_message(filters.command('title'), group=0)
async def title_message(_, message):
    user_id = message.from_user.id
    title = " ".join(message.command[1:])
    check = -1

    if title == '':
        await reply_and_delay_delete(message,  '語法 : `/title 你要的標題`', INFO_DELETE_TIME)
    elif title in black_list:
        await reply_and_delay_delete(message,  '不允許的頭銜', INFO_DELETE_TIME)
    else:
        check = _title.title(user_id)
    
    if check == 2:
        await reply_and_delay_delete(message,  '['+str(user_id)+'](tg://user?id='+str(user_id)+') 你好，查無此UID的簽到記錄。', INFO_DELETE_TIME)
    elif check == 0:
        await reply_and_delay_delete(message,  '['+str(user_id)+'](tg://user?id='+str(user_id)+') 你好，你的積分不滿足兌換需求。', INFO_DELETE_TIME)
    elif check == 1:
        try:
            await Client.promote_chat_member(_, message.chat.id, user_id)
            await Client.set_administrator_title(_, message.chat.id, user_id, title)
            await reply_and_delay_delete(message, '[' + str(user_id) + '](tg://user?id=' + str(user_id) + f') 已成功設置頭銜為 {title}', INFO_DELETE_TIME)
            _title.title_success(user_id)
        except:
            await reply_and_delay_delete(message, '[' + str(user_id) + '](tg://user?id=' + str(user_id) + ') 執行出錯了 嗚嗚嗚', INFO_DELETE_TIME)
    else:
        pass

