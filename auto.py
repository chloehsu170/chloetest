from widget import Widget
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
        print "11"
    def testSize(self):
        self.assertEqual(self.widget.getSize(),(50,50))

    def testResize(self):
        self.widget.setSize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))
    def tearDown(self):
        self.widget = None
        print "22"
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite
# def suite():
#     return unittest.makeSuite(WidgetTestCase, 'test')
if __name__ == "__main__":
    # unittest.main(defaultTest="suite")
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
