from widget1 import Widget1
import unittest

class Auto1(unittest.TestCase):
    def setUp(self):
        self.widget = Widget1()
    def testSize(self):
        self.assertEqual(self.widget.getSize(),(20,10))
    def tearDown(self):
        self.widget = None

def suite():
    suite = unittest.TestSuite
    suite.addTest("testSize")
    return suite
if __name__ == '__main__':
    unittest.main(defaultTest='suite')