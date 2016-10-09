import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "646567397@qq.com"
# receiver = "xuyanwen170@gmail.com"
receiver = "xu-yw@neusoft.com"
sendserver = "smtp.qq.com"
title = "python text email"
name = "646567397@qq.com"
# passwd = ""
passwd = "bfjoaxhpmgpybaja"
msg = MIMEText("你好！","text","utf-8")
msg['Subject'] = Header(title,"utf-8")

smtp =smtplib.SMTP_SSL("smtp.qq.com")
# smtp.connect()
smtp.login(name,passwd)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

