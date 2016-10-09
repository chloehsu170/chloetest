
__author__ = 'chloe'
# with open("abc.txt","r") as fp:
#     lines = fp.read()
    # print(lines.strip("\r\n"))
#     for line in lines:
# #         print(line.strip())
#         print(line.strip("\r\n"))
        # print(line.swapcase())
        # print(line.title())
        # print(line.translate("unic11"))
        # print(line.upper())
        # print((line.zfill(13)))

# with open("abc.txt","a") as af:
#     af.write("\n我叫张三")
# with open("abc.txt","r",encoding="gbk",errors="ignore") as bf:
#     # print(bf.read())
#     print(bf.read())

# from io import StringIO
# f = StringIO()
# f.write("abc\r\n")
# f.write("xyz")
# print(f.getvalue())
# fp = StringIO("中国\r\nXYW\nsla\nrer")
# while True:
#     line = fp.readline()
#     if line == '':
#         break
#     print(line)
# from io import BytesIO
# b = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd\xe9\x93\xb6\xe8\xa1\x8c')
# 10-01_22_03_12testResult.html', '2016-10-01_22_05_17testResult.html', 'abc.txt', 'AppData - 快捷方式.lnk', 'auto.py', 'auto1.py', 'autoMail.py', 'autoMail1.py', 'baidu1.py', 'blur.png
# print(b.getvalue())
# b.write("中国银行".encode("utf-8"))
# print(b.getvalue())
# print(b.read())
import os
# f = os.listdir()
# print(f)
# for ff in f:
#     s = os.path.splitext(ff)
#     # print(s)
#     if s[1] ==".py":
#         print(ff)
# s = ([ff  for ff in os.listdir() if os.path.splitext(ff)[1] ==".py"])
# print(s)
# print(len(s))
# ss = ([ff  for ff in os.listdir() if os.path.isfile(ff) and os.path.splitext(ff)[1] ==".py"])
# print(len(ss))
# os.system("dir >dir.txt 2>&1")
from datetime import datetime
# import os
# import numbers
# pwd = os.path.abspath(".")
# for f in os.listdir(pwd):
#     fsize = os.path.getsize(f)
#     # ftime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M")
#     ftime = datetime.fromordinal(numbers.Integral.cls)
#     if os.path.isdir(f):
#         flag = "<dir>"
#     else: flag = "     "
#     # print(ftime,flag, fsize,f)
#     print("%s %s %10d %s"%(ftime,flag,fsize,f))
# print(datetime.date(datetime.today()))#今天日期
# print(datetime.today())#今天
# print(datetime.time(datetime.today()).strftime("%H:%M:%S"))
import os,fnmatch,re
def test(pwd):
    f = os.listdir(pwd)
    # print(f)
    for file in f:
        path = os.path.join(pwd,file)
        # if os.path.isdir(file):
        #         test()
        if os.path.isfile(path):
            if fnmatch.fnmatch(file,"t*.py"):
                print(path)
            # if re.match(r"^[h-w]+",file):
            #     print(os.path.join(pwd,file))
        if os.path.isdir(path):
            test(path)
if __name__ == '__main__':
    pwd = os.path.abspath("f:\\")
    test(pwd)
