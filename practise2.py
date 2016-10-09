#-*-coding:utf-8-*- 
__author__ = 'chloe'
print('中文正常显示')
# def myabs(x):
#     if not isinstance(x,int):
#         raise "oprand type error."
#     if x > 0:
#         print(x)
#     else:
#         print(-x)
#
# # myabs(1)
# myabs(1.01)

# def append1(L = None):
#     if L is None:
#         L =[]
#     L.append('END')
#     print(L)
#
# append1([1])

# def calc1(*num):
#     s = 0
#     for i in num:
#         s = s+i*i
#     print(s)
# nums=(1,2,3,4)
# calc1(*nums)
#
# def enroll(name,age,sex='female',**kw):
#     print("name:",name,"age:",age,"sex:",sex,'others:',kw)
# others={'city':'shanghai','interest':'programming'}
# enroll('chloe',33,**others)
#
# def enroll(name,age,sex='female',*,city,interst='everything'):
#     print("name:",name,"age:",age,"sex:",sex,'city:',city,'interest:',interst)
# others={'city':'shanghai','interest':'programming'}
# enroll('chloe',33,interst=others['interest'],city=[])

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_visible(n):
    return lambda x:x%n >0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_visible(n),it)
for n in primes():
    if n<1000:
        print(n)
    else:
        break
