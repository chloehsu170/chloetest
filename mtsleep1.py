from multiprocessing import Process
import os

def info(title):
    print(title)
    print("module name:",__name__)
    if hasattr(os,"getppid"):
        print("parent id:",os.getppid())
    print("process id:",os.getpid())
def f(name):
    info("function f")
    print("hello",name)
if __name__ == '__main__':
    info("main line")
    p = Process(target= f,args=("chloe",))
    p.start()
    p.join()