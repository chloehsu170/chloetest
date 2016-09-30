# import telnetlib
# import  time
# Host = "localhost"
# username = "chloehsu"
# # port = '22'
# password = "abcd1234"
# finish =":~$"
#
# tn =telnetlib.Telnet(Host)
# # tn.read_until('login:')
# # print "login success!"
# tn.write(username +'\n')
# # tn.read_until('Password:')
# tn.write(password + '\n')
# # print "login success!!"
# # tn.read_until(finish)
# tn.write('ls'+ '\n')
# # print tn.read_until('>')
# # fp = open('ls.txt','w')
# fp.write(tn.read_all())
# fp.close()
# tn.read_until(finish)
# time.sleep(20)
# tn.close()
import telnetlib
import time
bot = telnetlib.Telnet("127.0.0.1", 22)
user = "chloehsu"
password = "abcd1234"
command ="ifconfig"
bot.write((user + "\n").encode('ascii'))
print(bot.read_all())
bot.write((password + "\n").encode('ascii'))
time.sleep(5)
bot.write((command +"\n").encode('ascii'))
bot.close()

# import socket
#
# s = socket.socket()
#
# host = raw_input("The ip you want to connect to: ")
# port = 22
#
# s.connect((host, port))
# print s.recv(1024)