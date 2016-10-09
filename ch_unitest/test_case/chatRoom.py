import telnetlib
import os
def do_telnet(Host,username, password,commands):
    tn = telnetlib.Telnet(Host)
    tn.set_debuglevel(3)
    #输入登录用户名
    tn.read_until(b"login: ")
    tn.write(username.encode("ascii")+b'\r\n')
    # 输入登录密码
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii")+b'\r\n')
    for item in commands:
        tn.write(item.encode("ascii")+b'\r\n')
    tn.write(b"exit\n")
    fp = open(os.getcwd() + '//a.txt', 'w')
    fp.write(tn.read_all().decode('ascii'))

    fp.close()
    tn.close()
if __name__=='__main__':
    Host = '192.168.226.133'
    username = 'chloehsu'
    password = 'abcd1234'
    commands = ['ifconfig', 'ls']
    do_telnet(Host, username, password,commands)