import time
try:
    file =open("poem.txt",'r')
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line
finally:
    file.close()
    print "cleaning up...clo"
