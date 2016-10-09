#-*-coding:utf-8-*- 
__author__ = 'chloe'
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# for data in [b'chloe',b'mary',b'sebil']:
#     s.sendto(data,('127.0.0.1',9999))
#     print(s.recv(1024).decode('utf-8'))
# s.close()

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'chloe',b'bob',b'ada']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()