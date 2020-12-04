#!usr/bin/env python
import socket

HOST = 'localhost'
PORT = 10000

def echo_sever():
    '''Echo Sever 的 Sever 端'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    
    while True:
        conn, addr = s.accept()
        print(f'Connectted by {addr}')
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
    s.close()

if __name__ == '__main__':
    echo_sever()