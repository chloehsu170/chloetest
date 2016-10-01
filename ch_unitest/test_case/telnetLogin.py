import telnetlib

user = "chloehsu"
password = "abcd1234"
# password = getpass.getpass()
comand = "ifconfig"
# finish = "~]$"
bot = telnetlib.Telnet("192.168.226.133")
bot.read_until(b"login:")
bot.write(user.encode('ascii') + b"\n")
bot.read_until(b"Password:")
bot.write(password.encode('ascii') + b"\n")
bot.write(b"ls -l\n")
bot.write(b"exit\n")
fp = open("telnetLogin2.txt","w")
fp.write(bot.read_all().decode('ascii'))
# print(bot.read_all().decode('ascii'))


