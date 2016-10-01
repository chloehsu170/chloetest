import os
aa = os.listdir("C:\\Users\\user\\chloetest\\ch_unitest\\test_case\\")
for a in aa:
    s = a.split(".")[1]
    if s == 'py':
        os.system("python C:\\Users\\user\\chloetest\\ch_unitest\\test_case\\%s >>log1.txt 2>&1" % a)