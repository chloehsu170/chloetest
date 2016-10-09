#-*-coding:utf-8-*- 
__author__ = 'chloe'
import os,fnmatch
# def test(pwd):
#     file = os.listdir(pwd)
#     for f in file:
#         path = os.path.join(pwd,f)
#         if os.path.isfile(path):
#             if fnmatch.fnmatch(f,"a*.py"):
#                 print(path)
#         if os.path.isdir(path):
#             test(path)
# if __name__ == '__main__':
#     pwd = os.getcwd()
#     test(pwd)
def test1(pwd):
    n = 0
    s = 0
    for root,dirs,files in os.walk(pwd):
        for file in files:
            if fnmatch.fnmatch(file,"t*.py"):
                print(os.path.join(root,file))
                n = n+1
        for dir in dirs:
            print(os.path.join(root,dir))
            s = s+1
    print(n)
    print(s)
if __name__ == '__main__':
    pwd = os.getcwd()
    test1(pwd)
