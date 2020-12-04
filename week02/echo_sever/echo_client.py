#!usr/bin/env python
import socket
import sys

HOST = 'localhost'
PORT = 10000

def echo_client():
    ''' Echo Sever 的 Client 端  '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    while True:
        data = open('file_exchange.txt', 'rb')
        if not data:
            break
        s.sendall(data.read())

        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
            text = data.decode("utf-8")
            with open('file_receive.txt', 'a+') as f:
                f.write(f'{text}\n')
            break
    s.close()

if __name__ == '__main__':
    echo_client()