# - * - coding: UTF-8 - * -
# import MySQLdb as mdb
import pymysql
import sys

con = pymysql.connect('localhost', 'root','abcd1234', 'testdb',charset ='utf8');

with con:
    cur = con.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS \
    #     user(id INT(20) PRIMARY KEY, name VARCHAR(20) character set gb2312)ENGINE=InnoDB")
    # cur.execute("CREATE TABLE IF NOT EXISTS \
    #     book(id INT(20) PRIMARY KEY, name VARCHAR(20) character set gb2312, uid INT(20), CONSTRAINT book_ibfk_1 FOREIGN KEY (uid) REFERENCES user(id) ON DELETE CASCADE  ON UPDATE CASCADE)ENGINE=InnoDB")
    cur.execute("INSERT INTO book (id,name,uid) VALUES(1,'math',1)")
    cur.execute("INSERT INTO book (id,name,uid) VALUES(2,'suan',1)")
    # cur.execute("INSERT INTO user (id,name) VALUES(1,'杭飒')")
    # cur.execute("CREATE TABLE IF NOT EXISTS \
    # #     user(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(20) character set gb2312, Uid VARCHAR(20),CONSTRAINT FOREIGN KEY (Uid) REFERENCES book(Id) )")
    # # cur.execute("INSERT INTO maths (Name) VALUES('杭飒')")
    # cur.execute("INSERT INTO maths(Name) VALUES('zhangsan')")
    # cur.execute("INSERT INTO maths(Name) VALUES('李四')")
    # cur.execute("INSERT INTO maths(Name) VALUES('王五')")
    # cur.execute("INSERT INTO maths(Name) VALUES('马六')")

    # cur.execute("drop table book")
    # cur.execute("drop table user")