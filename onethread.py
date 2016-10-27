from time import sleep,ctime
def loop0():
    print('start loop 0 at :',ctime())
    sleep(4)
    print('loop 0 is done at :',ctime())
def loop1():
    print('start loop 1 at :',ctime())
    sleep(4)
    print('loop 1 is done at :',ctime())
if __name__ == '__main__':
    loop0()
    loop1()
    print('all loops are done at :',ctime())