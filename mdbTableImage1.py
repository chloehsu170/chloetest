import  MySQLdb as  mdb

conn = mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur =conn.cursor()
aa =cur.execute("select image from image")

file =open('image.png','wb')
file.write(cur.fetchone()[0])

conn.close()