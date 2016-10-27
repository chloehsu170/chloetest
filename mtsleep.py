from time import sleep,ctime
import threading

nloops = [4,2]
threads = []
def loop(nloop,nsec):
    print("now start loop" ,nloop,ctime())
    sleep(nsec)
    print("now start"+ "loop" ,nloop,ctime())
def main():
    aa = len(nloops)
    for i in range(aa):
        t = threading.Thread(target=loop,args=(i,nloops[i]))
        threads.append(t)
    for i in range(aa):
        threads[i].start()
    for i in range(aa):
        threads[i].join()
    print('all threads is done',ctime())
if __name__ == '__main__':
    main()
