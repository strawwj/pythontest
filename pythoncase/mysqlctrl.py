import pymysql
class MySqlCtrl():
    def __init__(self,host,db):
        self.host = host
        self.db = db
        self.conn = pymysql.connect(host = '{}'.format(self.host),password ='wj042397',db = '{}'.format(self.db))
        self.cur = self.conn.cursor()
    def insert(self,cid,cname):
        self.cid = cid
        self.cname = cname
        self.cur.execute("insert into class(cid,cname) value(%s,%s)",(self.cid,self.cname))
        self.conn.commit()
    def delete(self,n):
        self.n = n
        self.cur.execute("delete from class where cid = (%s)",(self.n))
        self.conn.commit()
    def update(self,m,ne):
        self.ne = ne
        self.m = m
        self.cur.execute("update  class  set cname = (%s) where cname = (%s)",( self.m,self.ne))
        self.conn.commit()
    def select(self):
        s = self.cur.execute("select * from student")
        i = 0
        while i < s: 
            print(self.cur.fetchmany())
            i += 1
            if i == s:
                self.cur.scroll(-s)  
    def __del__(self):
        self.cur.close()
        self.cur.close()
ms = MySqlCtrl("localhost","mytest")
#ms.insert('5',"wu ban")
#ms.delete("5")
ms.update("four ban","si ban")
ms.select()
ms1 = MySqlCtrl("localhost","mytest")
ms1.select()
