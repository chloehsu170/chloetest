#!/usr/bin/python
# -*- coding: utf-8 -*-

# import  MySQLdb
import pymysql
db = None
db =pymysql.connect('localhost', 'root','abcd1234', 'testdb',charset='utf8')
cursor = db.cursor()
cursor.execute("select name from user")
data = cursor.fetchall()
for d in data:
    # print(d[0].decode('utf-8'))
    print(d)
# print("MySQL new name is: %s" % data)
db.close()
# 192.168.8.103