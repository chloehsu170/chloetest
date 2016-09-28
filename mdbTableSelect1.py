import MySQLdb as mdb

conn =mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur = conn.cursor()
aa=cur.execute("select * from student")
desc =cur.description
print desc[1][0],desc[3][0]
# aa = int(cur.rowcount)
for i in range(aa):
    row = cur.fetchone()
    print row[1],row[3]
    print "%2s,%3s" % (row[1],row[3])
conn.close()