import HTMLTestRunner
import unittest
import time,sys,os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# sys.path.append("//ch_unitest//")
listaa = "C://Users//chloe//AppData//Local//Programs//Python//Python35//chloetest//ch_unitest//"
suite = unittest.defaultTestLoader.discover(start_dir=listaa,pattern="start*.py",top_level_dir=None)

now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
fp = open(now + "report.html","wb")
runner = HTMLTestRunner.HTMLTestRunner(stream= fp,
                                       title=u'test report',
                                       description=u'details are as followed:')
runner.run(suite)

