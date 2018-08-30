from threading import Thread
import queue
import subprocess
queue = queue.Queue()
def get_Ip():
    for i in range(1,254):
        ip = '172.25.2.{}'.format(i)
        #print(ip)
        ret = subprocess.call('ping -c 1 {}'.format(queue.get(ip)),shell = True,stdout=open('/dev/NULL','w'),stderr=subprocess.STDOUT)
        print(ret)
        if ret == '0':
           print('连接成功')
        elif ret == '1':
           print('失败')
        elif ret == '2':
           print('出错误')
get_Ip()
