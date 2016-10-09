#-*-coding:utf-8-*- 
__author__ = 'chloe'
# import socket,time
# import threading
# def tcplink(sock,addr):
#     print('accept from client %s:%s'% addr)
#     sock.send(b'welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(3)
#         if not data or data == b"exit":
#             break
#         sock.send(('hello %s'% data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print("connection from %s:%s closed."% addr)
# # if __name__ == '__main__':
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("127.0.0.1",8999))
# s.listen(5)
# print("waiting for connection.")
# while True:
#     sock,addr = s.accept()
#     t = threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()
import socket,time,threading
def tcplink(sock,addr):
    print("accept data from %s:%s"% addr)
    while True:
        data = sock.recv(1024)
        time.sleep(3)
        if not data or data == b'exit':
            break
        sock.send(("hello,%s"% data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("connection from %s:%s closed."% addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print("waiting for connection...")
while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()