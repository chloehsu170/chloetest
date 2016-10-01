import telnetlib
import time
# from signal import signal,  SIG_DFL
# signal(SIG_DFL)

user = "chloehsu"
password = "abcd1234"
comand = "ifconfig"
finish = "~]$"
bot = telnetlib.Telnet("192.168.226.133")
# print(bot.read_all())
bot.read_until(b"login:")
time.sleep(2)
bot.write(user.encode('ascii') + b"\n")
time.sleep(2)
# print(bot.read_all())
bot.read_until(b"Password:")
# time.sleep(5)
bot.write(password.encode('ascii') + b"\n")
# print(bot.read_all())
# bot.read_until((finish).encode('ascii'))
time.sleep(2)
bot.write(b"ls\n")
bot.write(b"exit\n")
print(bot.read_all().decode('ascii'))


