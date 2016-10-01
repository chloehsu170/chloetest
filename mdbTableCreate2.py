import MySQLdb as mdb

conn = mdb.connect('192.168.32.128','tester','abcd1234','testdb')
cur =conn.cursor()
cur.execute("create table student(id int,name varchar(20),class varchar(30),age varchar(10))")
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
cur.execute("insert into student values('3','Mary','3 year 2 class','10')")
cur.execute("update student set class ='3 year 1 class' where name ='Tom'")
cur.execute("delete from student where age ='10'")
cur.close()
conn.commit()
conn.close()