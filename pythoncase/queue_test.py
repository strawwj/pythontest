from threading import Thread
import queue
queue = queue.Queue()
import subprocess
def pinger(i,q):
    while True:
        ip = q.get()
        print('Thread %s Pinging:%s'%(i,ip))
        ret = subprocess.call('ping -c 1 {}'.format(ip),shell=True,stdout=open('/dev/NULL','w'),stderr=subprocess.STDOUT)
        if ret == 0:
            print('连接成功 {}'.format(ip))
        else:
            print('连接失败{}'.format(ip))
        queue.task_done()
ips = []
for i in range(1,255):
    ips.append('172.25.2.{}'.format(i))
for ip in ips:
    queue.put(ip) 

for i in range(10):
    th = Thread(target=pinger,args=(i,queue))
    th.setDaemon(True)
    th.start()
print('Main Thread waiting...')
queue.join()
print('Done')    
