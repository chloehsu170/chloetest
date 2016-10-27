#-*-coding:utf-8-*- 
__author__ = 'chloe'
from multiprocessing import Process,Queue
# from queue import Queue
import os,time,random
from ch_unitest import all_tests3
# def write(q):
#     print('process to write: %s'% os.getpid(),time.time())
#     for value in ['a','b','c']:
#         print('put %s to queue...'% value,time.time())
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('process to read: %s'% os.getpid(),time.time())
#     while True:
#         value = q.get()
#         print('get %s from queue.'% value,time.time())
if __name__ == '__main__':
    q = Queue()
    # write(q)
    # read(q)
    # q.close()
    pw = Process(target=all_tests3.autoTestReport,args=(q,))
    # pr = Process(target=read,args=(q,))
    pw.start()
    # pr.start()
    pw.join()
    # pr.terminate()

# def write(q):
#     print('process to write: %s'% os.getpid(),time.time())
#     for value in ['a','b','c']:
#         print('put %s to queue...'% value,time.time())
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('process to read: %s'% os.getpid(),time.time())
#     while True:
#         value = q.get()
#         print('get %s from queue.'% value,time.time())
# if __name__ == '__main__':
#     print("parent process is %s"% os.getpid())
#     pid = os.fork()
#     print("subprocess is %s"% pid)
#     pid = os.fork()
#     print("subprocess is %s"% pid)
#     q = Queue()
#     write(q)
#     read(q)
#     q.close()
