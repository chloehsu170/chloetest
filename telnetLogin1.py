# coding=utf-8
import sys
import telnetlib
import time

host = '192.168.32.128'
user = 'root'
PASS = b'1'
cmd = b"dir rn"
tn =telnetlib.Telnet(host)
tn.set_debuglevel(0)
print "waiting..."
time.sleep(5)
tn.