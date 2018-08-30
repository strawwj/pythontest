#udp没有客户端服务端之分
import socket
MYHOST = '127.0.0.1'
OTHERHOST = '127.0.0.1'
PORT = 60008
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((MYHOST,PORT))
    s.sendto(b'hello i am wj',(OTHERHOST,60008))
    data,addr = s.recvfrom(1024)
    print('data:',data)
    print('addr:',addr)
    s.close()
