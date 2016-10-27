#coding=utf-8
import HTMLTestRunner
import time
import unittest
from ch_unitest.test_case import *
from ch_unitest.test_suite import *
# import ff_selenium_ide
# import baidu

suite =  unittest.TestSuite()
# suite.addTest(Baidu("test_xxx"))
testcases = [ff_selenium_ide.FfSeleniumIde,baidu.Baidu]
for testcase in testcases:
    suite.addTest(unittest.makeSuite(testcase))
# suite.addTest(unittest.makeSuite(ff_selenium_ide.FfSeleniumIde))
# suite.addTest(unittest.makeSuite(baidu.Baidu))
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
fp = open(now+'testResult.html','wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'综合测试报告1',
    description = u'测试情况如下说明1:'
)

runner.run(suite)