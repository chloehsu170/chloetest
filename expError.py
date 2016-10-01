try:
    open('abc.txt','r')
except IOError:
    pass
# print aa
try:
    print aa
except NameError,msg:
    print msg