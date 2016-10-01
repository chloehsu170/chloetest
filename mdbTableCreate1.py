#!/usr/bin/python
# -*- coding: utf-8 -*-

import  MySQLdb
db = None
db =MySQLdb.connect('192.168.32.128','root','abcd1234','mysql')
cursor = db.cursor()
cursor.execute("select user from user where user ='chloe'")
data = cursor.fetchone()
print "MySQL new name is: %s" % data
db.close()