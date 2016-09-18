__author__ = 'chloe'
#可变参数
def calc(*num):
    s = 1
    for n in num:
        s = s * n
    print(s)
ww = (1,2,3,4)
print(ww)
calc(*ww)
#关键字参数
def person(name,age,**other):
    print('name:',name,'age:',age,other)
other={'city':'shanghai','job':'it'}
person('chloe',18,**other)
#命名关键字参数
def person1(name,age,*,city='shanghai',job):
    print(name,age,city,job)
person1('chloe',33)