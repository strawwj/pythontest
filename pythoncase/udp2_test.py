#Echo client program
import threading
import socket
PORT = 60000
HOST = '10.0.2.15'
import struct
def sent(sock,addr):
    i_say = ''
    while i_say != 'bye':
        i_say = input('i say:')
        sock.sendto(i_say.encode('utf-8'),addr)
def recv(sock):
    while True:
        other_say,addr=sock.recvfrom(1024)
        print('{} say> {}'.format(addr[0],other_say.decode('utf-8')))
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
ipaddr = input('you want say to :')
addr = (ipaddr,60000)
            
if __name__ == '__main__':        
    t1 = threading.Thread(target=sent,args=(s,addr))
    t1.setDaemon(True)
    t1.start()
    t2 = threading.Thread(target=recv,args=(s,))
    t2.setDaemon(True)
    t2.start()
    t1.join()
    t2.join()
