import pymysql
from config import config

def db_query(sql, values=None):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password=config['MYSQL_PASSWORD'], db=config['DATABASE_NAME'],
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql, values)
        result = cursor.fetchall()
        conn.commit()
    except:
        result = None
        conn.rollback()
    cursor.close()
    conn.close()
    return result