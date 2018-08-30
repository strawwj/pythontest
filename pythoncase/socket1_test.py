# Echo client program
import socket

HOST = '172.25.9.145'    # The remote host
PORT = 5001              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#同一协议
    s.connect((HOST, PORT))
    text = 'ZWCKLG3E346PN4CI.jpg'
    with open('{}'.format(text),'rb') as f:
        while True:
            f1 = f.read(1024)
            if f1:
                s.send(f1)
            else:
                break

