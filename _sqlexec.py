from _config import SQL_HOST, SQL_USER, SQL_PASS, SQL_DB
import mysql.connector
import datetime
import re
import time

conn = mysql.connector.connect(
    host = SQL_HOST, 
    database = SQL_DB,
    user = SQL_USER, 
    password = SQL_PASS,
    #ssl_disabled=False,
)

def title_success(uid):
    with conn.cursor() as cursor:
        update_query = f"UPDATE {SQL_DB} SET score = score-50 WHERE id = "+str(uid)+';'
        cursor.execute(update_query)
        conn.commit()

def title(uid):
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {SQL_DB} WHERE id = " + str(uid) + ';'
            cursor.execute(query)
            existing_user = cursor.fetchone()

            if existing_user:
                queryLast = f"SELECT score FROM {SQL_DB} WHERE id = " + str(uid) + ';'
                cursor.execute(queryLast)
                qScore = keepInt(cursor.fetchall())
                if qScore < 50:
                    return 0
                else:
                    return 1
            else:
                return 2
    except Exception as e:
        print(f"Error: {e}")
        return('數據庫發生錯誤')

def lb():
    try:
        with conn.cursor() as cursor:
            query = f"SELECT id, times FROM {SQL_DB} order by times DESC LIMIT 5;"
            cursor.execute(query)
            result = cursor.fetchall()
            d1=''
            for item in result:
                d1=d1+"UID {} 累積簽到 {} 次".format(item[0], item[1])+'\n'
            return 'Top 5\n\n'+d1
    except Exception as e:
        print(f"Error: {e}")
        return('數據庫發生錯誤')

def me(uid):
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {SQL_DB} WHERE id = " + str(uid)+';'
            cursor.execute(query)
            result = cursor.fetchall()
            for item in result:
                id_, time, score, passed = item
            return f"""```
上次簽到時間為 {datetime.datetime.fromtimestamp(time)}
目前的積分為 {score}
累積簽到次數為 {passed}
```
"""
    except Exception as e:
        print(f"Error: {e}")
        return('數據庫發生錯誤')


def q(uid, luck):
    last = int(time.time())
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {SQL_DB} WHERE id = " + str(uid)
            cursor.execute(query)
            existing_user = cursor.fetchone()

            if existing_user:
                queryLast = f"SELECT last FROM {SQL_DB} WHERE id = " + str(uid) + ';'
                cursor.execute(queryLast)
                qLast = keepInt(cursor.fetchall())
                rq = last-qLast
                if rq < 86400:
                    return('你已經簽到過了，請於 '+str(int((86400-(rq))/3600))+' 小時 '+str(int(((86400-(rq))%3600)/60))+' 分後重試。')
                else:
                    update_query = f"UPDATE {SQL_DB} SET times = times + 1, score = score+"+str(luck)+", last = "+str(last)+" WHERE id = "+str(uid) +';'
                    cursor.execute(update_query)
                    conn.commit()
                    cursor.execute(f'SELECT times from {SQL_DB} ]WHERE id = '+str(uid) +';')
                    return("這是你第 "+str(keepInt(cursor.fetchall()))+"次簽到，本次簽到獲得 "+str(luck)+" 分")
            else:
                insert_query = f"INSERT INTO {SQL_DB} Values("+str(uid)+","+str(last)+","+str(luck)+",1) ;"
                cursor.execute(insert_query)
                conn.commit()
                return('這是你第 1 次簽到，本次簽到獲得 '+str(luck)+' 分')
    except Exception as e:
        print(f"Error: {e}")
        return('數據庫發生錯誤')
    

def keepInt(inputData):
    return int(re.sub(r'[^0-9]', '', str(inputData)))
