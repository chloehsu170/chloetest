from selenium import webdriver
import defLogin,defQuit
import unittest

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://www.baidu.com"

    def testLogin(self):
        driver = self.driver
        driver.get(self.url)
        defLogin.login(self)

    def tearDown(self):
        # self.driver.quit()
        defQuit.quit(self)

if __name__ == "__main__":
    unittest.main()




