import MySQLdb as mdb
import sys

file = open("error.png",'rb')
img = file.read()
file.close()
# file1 = open("soup.png",'wb')
# file1.write(img)
# file1.close()
conn = mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur = conn.cursor()
# cur.execute("create table image(id int,image mediumblob)")
# sqli ="insert into image values(%s,%s)"
# cur.execute(sqli,('1',mdb.escape_string(img)))
cur.execute("INSERT INTO image SET image='%s'" % \
               mdb.escape_string(img))

cur.close()
conn.commit()
conn.close()