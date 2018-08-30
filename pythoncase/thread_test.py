'''
import threading
class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print('this is {}'.format(self.name))
t1 = MyThread('T1')
t2 = MyThread('T2')
t1.start()
'''
import threading
import time
def func(name,n):
    for i in range(n):
        print(name,i)
        time.sleep(0.5)
    
   # func('t1')
   # func('t2')
   # func('t3')
    
t1 = threading.Thread(target=func, args=('t1',5))
t2 = threading.Thread(target=func, args=('t2',10))
t3 = threading.Thread(target=func, args=('t3',10))
t1.start()#启动线程
t1.join() # 保证t1先执行完
#t2.daemon = True#当进程结束时，线程跟着结束(默认：进程等待线程结束)
t2.start()
print('t2 name:',t2.getName())
print("t2 setname:",t2.setName('tttt222'))
print('t2 name:',t2.getName())
print(t2.isDaemon())
t2.join()
#t3.daemon = True
t3.start()
print(t3.isAlive())#检验t3是否存活
#t3.join()
print('main end')#进程执行，看join结束时加入线程的执行

