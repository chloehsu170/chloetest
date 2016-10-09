#-*-coding:utf-8-*- 
__author__ = 'chloe'
# import socket,time
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',9999))
# print('Bind UDP on 9999...')
# while True:
#     data,addr = s.recvfrom(1024)
#     time.sleep(3)
#     print("received data from %s:%s"% addr)
#     s.sendto(b"hello %s."% data,addr)
import socket,time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print("binding udp on 9999")
while True:
    data,addr = s.recvfrom(1024)
    time.sleep(3)
    print("accept data from %s:%s"% addr)
    s.sendto(b"hello %s"% data,addr)