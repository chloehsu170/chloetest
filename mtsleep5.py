from multiprocessing import Process
import os

def run_proc(name):
    print("child process %s(%s) is start..." % (name,os.getpid()))
if __name__ == '__main__':
    print("parent process %s is start now..."% os.getpid())
    p1 = Process(target=run_proc,args=("test1",))
    p2 = Process(target=run_proc,args=("test2",))
    print('child process will start.')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("child process end now.")