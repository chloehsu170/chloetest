import HTMLTestRunner
import all_testcases
import unittest
import time
suite = unittest.TestSuite()
allcases =all_testcases.all_testcases()
for case in allcases:
    suite.addTest(unittest.makeSuite(case))
now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
fp = open(now+"testResultReport.html","wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u"综合测试报告",
                                       description=u"测试情况如下说明：")
runner.run(suite)
