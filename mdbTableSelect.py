import MySQLdb as mdb

conn = mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur = conn.cursor()
aa = cur.execute("select * from student")
print aa
info = cur.fetchall()
# info = cur.fetchmany(aa)
for ii in info:
    print ii
conn.close()