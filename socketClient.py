#-*-coding:utf-8-*- 
__author__ = 'chloe'
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',8999))
# print(s.recv(1024).decode('utf-8'))
# for data in [b'chloe',b'mary',b'bob']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",9999))
# print(s.recv(1024).decode("utf-8"))
for data in [b'chloe',b'ada',b'mary']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()