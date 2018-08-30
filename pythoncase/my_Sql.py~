import pymysql
sql_i = """
        insert into new value(%s, %s)
        """
i = input('id')
n = input('name')
conn = pymysql.connect(password = 'wj042397',db = 'auth')
cur = conn.cursor()
cur.execute(sql_i,(i,n))
cur.execute('flush privileges')
cur.close()
conn.close()
