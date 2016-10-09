#-*-coding:utf-8-*-
__author__ = 'chloe'
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("www.baidu.com",80))
# s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: Close\r\n\r\n')
# buffer = []
# while True:
#     b = s.recv(1024)
#     if b:
#         buffer.append(b)
#     else:
#         break
# s.close()
# data = b''.join(buffer)
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open("baidu3.html","wb") as f:
#     f.write(html)
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.sina.com",80))
s.send(b"GET / HTTP/1.1\r\nHost:www.sina.com\r\nConnection: Close\r\n\r\n\r\n")
buffer = []
while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
s.close()
b =b''.join(buffer)
header,html = b.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open("baidu11.html","wb") as fb:
    fb.write(html)
