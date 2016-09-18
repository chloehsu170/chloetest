__author__ = 'chloe'
import math
print(math.pi)
print(12%3)
print(ord('A'))
print(chr(65))
print(len('中文'.encode('utf-8')))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
name=input("please input your name:")
age=input("please input your age:")
Age= int(age)
if Age >= 18:
    print('''hello adult:''',name,
    '''your age is:''',Age)
else:
    print('''hello teenager's name is''',name,
    '''your age is:\n''',Age)
