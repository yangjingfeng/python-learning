# import pymysql

# conn = pymysql.Connect('192.168.1.230','mydb','mydb','test',3306)
# cur = conn.cursor()
# id = "2 or 1 = 1"
# sqlclause = "select * from t where id={}".format(id)
# cur.execute(sqlclause)
# for line in cur.fetchall():
#     print(line)

# conn = pymysql.Connect('192.168.1.230','mydb','mydb','test',3306)
# cur = conn.cursor()
# # id = "2 or 1 = 1"
# d = {'id':'2 or 1 = 1'}
# sqlclause = "select * from t where id=%(id)s"
# cur.execute(sqlclause,args=d)
# for line in cur.fetchall():
#     print(line)
# print('aaaa')
# with conn.cursor() as cur:
#     d = {'id':'2 '}
#     sqlclause = "select * from t where id=%(id)s"
#     cur.execute(sqlclause,args=d)
#     for line in cur.fetchall():
#         print(line)
#     print('aaaa')
#
# import pymysql
# conn = pymysql.Connect('192.168.1.230','mydb','mydb','test',3306)
# with conn as cursor:
#     with cursor:
#         cursor.execute('select * from t')
#         for line in cursor.fetchall():
#             print(line)
from queue import Queue
import pymysql
import time
class ConnPool:
    def __init__(self, maxsize,*args):
        self.maxsize = maxsize
        self._pool = Queue(maxsize)
        for i in range(maxsize):
            conn = pymysql.connect(*args)
            self._pool.put(conn)

    def get_conn(self):
        return self._pool.get()
    def ret_conn(self, conn:pymysql.connections.Connection):
        if isinstance(conn,(pymysql.connections.Connection)):
            self._pool.put(conn)
    @property
    def cursize(self):
        return self._pool.qsize()

pool = ConnPool(5,'192.168.1.230','mydb','mydb','test',3306)
s = pool.get_conn()
print(s)
time.sleep(1)

with s as cursor:
    cursor.execute()
