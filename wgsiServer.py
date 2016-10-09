#-*-coding:utf-8-*- 
__author__ = 'chloe'
# from wsgiref.simple_server import make_server
# def application(environ,start_response):
#     start_response('200 OK',[('Content-Type','text/html')])
#     return [b'<h1>hello web!</h1>']
# httpd =make_server('0.0.0.0',8000,application)
# print("serving HTTP on 8000...")
# httpd.serve_forever()
from wsgiref.simple_server import make_server
def application(environ,start_response):

    start_response("200 OK",[('Content-Type','text/html')])
    body = '<h1>hello,%s</h1>'% (environ['PATH_INFO'][1:] or  'web')
    return [body.encode('utf-8')]
    # return [b'<h1>hello chloe, welcome to chloe web!</h1>']
httpd = make_server('',8080,application)
print("serving HTTP on 8080...")