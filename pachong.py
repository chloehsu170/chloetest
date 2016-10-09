#-*-coding:utf-8-*- 
__author__ = 'chloe'
# from urllib import request
# response = request.urlopen('http://www.baidu.com')
# print(response.read())
def log(func):
    def wrapper(*args,**kw):
        print('call %s:'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2016-10-4')