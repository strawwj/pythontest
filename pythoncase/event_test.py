'''
import threading
import time
def worker(event,name):
    while not event.is_set():
        print('({})waitting to test MySQL connect......'.format(name))
        event.wait(1)#数据库连接上了才执行下面的
    
    #time.sleep(2)
    print('({})MySQL ready,now you can connect MySQL Server'.format(name))
    print('connected MySQL')
evt_mysql=threading.Event()
t1 = threading.Thread(target= worker,args=(evt_mysql,'t1'))
t1.start()
t2 = threading.Thread(target= worker,args=(evt_mysql,'t2'))
t2.start()
print('First of all, i am connecting mysql')
time.sleep(6)
print('ok')
evt_mysql.set()#set 给wait发送信号
'''


import threading
import time
def worker(event,name):
    while not event.is_set():
        print('({})waitting to test MySQL connect......'.format(name))
        event.wait(1)#数据库连接上了才执行下面的
    #time.sleep(2)
    print('({})MySQL ready,now you can connect MySQL Server'.format(name))
    print('connected MySQL')
def seter(event,t,name):
    print('First of all, I am connecting mysql')
    time.sleep(t)
    print('{} ok'.format(name))
    event.set()
evt_mysql = threading.Event()
s1 = threading.Thread(target = seter,args=(evt_mysql,3,'s1'))
s1.start()
s2 = threading.Thread(target = seter,args=(evt_mysql,1,'s2'))
s2.start()
t1 = threading.Thread(target= worker,args=(evt_mysql,'t1'))
t1.start()
t2 = threading.Thread(target= worker,args=(evt_mysql,'t2'))
t2.start()
