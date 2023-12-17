from _config import SQL_HOST, SQL_USER, SQL_PASS, SQL_DB
import mysql.connector

conn = mysql.connector.connect(
    host='SQL_HOST', 
    user='SQL_USER', 
    password='SQL_PASS',
)
cursor = conn.cursor()
cursor.execute(f"USE {SQL_DB};")


conn.close()


