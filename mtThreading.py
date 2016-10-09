#-*-coding:utf-8-*- 
__author__ = 'chloe'
import threading,time
def loop(thr):
    print('thread %s is running...'% thr)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (thr,n))
        time.sleep(1)
    print('thread %s ended.'% thr)

print('thread %s is running...'% threading.current_thread().name)
t1 = threading.Thread(target=loop,args=('thr1',))
t2 = threading.Thread(target=loop,args=('thr2',))
t1.start()
t2.start()
t1.join()
t2.join()
print('thread %s ended.'% threading.current_thread().name)