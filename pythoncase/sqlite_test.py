'''
import os
import sqlite3
conn = sqlite3.connect('hero.db')
os.getcwd
cur = conn.cursor()
cur.execute("create table player (id int,name char(20),passwd varchar(30))")
cur.execute("insert into player values(1,'my','13213')")
conn.commit()
'''

import sqlite3
conn = sqlite3.connect('hero.db')
cur = conn.cursor()
a = cur.execute("select * from player")
conn.commit()
cur.fetchone()
