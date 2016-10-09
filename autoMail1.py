import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '646567397@qq.com'
receiver = 'xu-yw@neusoft.com'
smtpserver = 'smtp.qq.com'
title = 'python mail'
username = '646567397@qq.com'
passwd =  'bfjoaxhpmgpybaja'
msg = MIMEText("<html><h1>你好！！</h1></html>","html","utf-8")
msg['Subject'] = Header(title,"utf-8")
smtp = smtplib.SMTP_SSL(smtpserver)
smtp.login(username,passwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()