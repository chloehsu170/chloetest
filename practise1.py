#-*-coding:utf-8-*-
__author__ = 'chloe'
from sqlalchemy import Column,String,create_engine,ForeignKey,INT
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import  declarative_base

# create object's base class'
Base = declarative_base()
# define Maths object

class Book(Base):
    __tablename__ = 'book'

    id = Column(INT, primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    uid = Column(INT, ForeignKey('user.id'))

class Users(Base):
    # table name
    __tablename__ = 'user'
    # talbe structor
    id = Column(INT,primary_key=True)
    name = Column(String(20))
    book = relationship('Book')

# initial database connection
engine = create_engine('mysql+pymysql://root:abcd1234@localhost:3306/testdb?charset=utf8')
# create DBSession TYPE
DBSession = sessionmaker(bind=engine)

# create object of session
session = DBSession()
# create Maths object
# new_maths = Maths(id ='9',name='sebil')
# add into session
# session.add(new_maths)
# user = Users(id='1',name='chloe',book=[book1,book2])
# user = Users(id=2,name='chloe')
# session.add(user)
# session.commit()
# book1 = Book(id=3,name ='maths',uid =2)
# session.add(book1)
# session.commit()
# book2 = Book(id=4,name ='python',uid =2)
# session.add(book2)
# session.commit()
#
# session.close()

session = DBSession()
user = session.query(Users).filter(Users.id ==2).one()
print('type:',type(user))
print('name:',user.name)
print('books:',user.book)
session.close()




#     def __init__(self,id,name):
#         self.id =  id
#         self.name = name
#
# [
#     User('1','chloe'),
#     User('2','mary'),
#     User('3','bob')
# ]