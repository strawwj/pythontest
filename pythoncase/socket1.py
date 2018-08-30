import socket
import threading
MYHOST = '127.0.0.1'
PORT = 60008
def checkPort(event,address,sock):
    l = []
    sock.sendto(b'hello i am wj',('10.0.2.15',60008))
    event.wait(5)
    data=sock.recvfrom(1024)
    print(b'data:',data)
    if not data:
        print("connection to %s on port %s failed"%(address,60008))
    else:
        print("connected !!!")
        l.append(ip)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((MYHOST,PORT))
evt=threading.Event()
with open('/root/ip.txt') as f:
    f1 = f.readlines()
    for ip in f1:
        print(ip)
        checkPort(evt,ip,s)
        evt.set()
        
'''
for i in range(100):
    t = Thread(target=checkPort,args=(ip,s))
    t.setDaemon(True)
    t.start()
'''
print(l)
