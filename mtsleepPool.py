from multiprocessing import Pool
import os,time,random

def run_poolproc(name):
    print("child process %s(%s) is running..."% (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("child process %s runs %s seconds."% (name,end-start))
if __name__ == '__main__':
    print("parent process %s."% os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(run_poolproc,args=(i,))
    print("waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")
