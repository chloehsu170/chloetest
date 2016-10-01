import MySQLdb as mdb

conn = mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur =conn.cursor()
sqli = 'insert into student values(%s,%s,%s,%s)'
cur.executemany(sqli,[('5','Gob','2 year 1 class','7'),
                      ('6','Mary','2 year 2 class','7'),
                      ('7','Bio','2 year 3 class','7'),
                      ('8','Doh','2 year 4 class','7')])
cur.close()
conn.commit()
conn.close()