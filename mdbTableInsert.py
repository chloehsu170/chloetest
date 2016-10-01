import MySQLdb as mdb

conn =mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur =conn.cursor()
sqli = "insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,('4','Bob','2 year 1 class','7'))
cur.close()
conn.commit()
conn.close()


