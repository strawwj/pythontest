#Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port 0-65535
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#AF_INET：IPV4 SOCK_STREAM:TCP 创建套接字对象
    s.bind((HOST, PORT)) #host当前服务器的地址，port端口号元组
    s.listen(1)
    conn, addr = s.accept()#等待连接 ，conn通道
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)#接收客户端的数据，1024缓冲大小
            if not data: break
            conn.sendall(data)
