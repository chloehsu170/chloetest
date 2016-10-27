import HTMLTestRunner
import unittest
import time,os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from multiprocessing import Process,Queue
def sendFile():
    path_dir = "C:\\Users\\chloe\\AppData\\Local\\Programs\\Python\\Python35\\chloetest\\ch_unitest\\test_report"
    list = os.listdir(path_dir)
    list.sort(key=lambda fn:os.path.getmtime(path_dir+'//'+fn))
    newfile = os.path.join(path_dir,list[-1])
    print(newfile)
    return newfile
def sendMail():
    sender = "646567397@qq.com"
    receiver = "xu-yw@neusoft.com"
    title = " Python Test Report"
    smtpserver = "smtp.qq.com"
    username = "646567397@qq.com"
    passwd = "bfjoaxhpmgpybaja"
    with open(sendFile(),"rb") as new_file:
        newfile = new_file.read()
        print(new_file.mode,new_file.name,new_file.closed)
    msg = MIMEText(_text=newfile,_subtype="html",_charset="utf-8")
    msg['Subject'] = Header(title,"utf-8")
    msg['data'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    smtp = smtplib.SMTP_SSL(smtpserver)
    smtp.login(username,passwd)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("Test report is sent successfully!!")

def autoTestReport():
    # sys.path.append("//h_unitest//")
    listaa = "C://Users//chloe//AppData//Local//Programs//Python//Python35//chloetest//ch_unitest//"
    suite = unittest.defaultTestLoader.discover(start_dir=listaa,pattern="start*.py",top_level_dir=None)

    now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    with open("test_report//"+now + "report.html","wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream= fp,
                                           title=u'test report',
                                           description=u'details are as followed:')
        # proc = Process(target=runner.run,args=(i,))
        # proc.start()
        # proc.join()
        runner.run(suite)
    # fp.close()
    print("Test report is done now!!")
if __name__ == '__main__':
    autoTestReport()
    # sendMail()