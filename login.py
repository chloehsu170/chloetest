#coding=utf-8
from splinter import Browser
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def log_in_doban(Name = '', PassWrod = ''):
  if Name and PassWrod:
    bs = Browser('chrome')
    bs.visit(url='http://10.10.10.28:9080/ssenewtrain/pages/frontend/login.jsp')
    if bs.is_element_present_by_id(id='username1'):
      bs.find_by_id(id='username1').fill(Name)
      bs.find_by_id(id='password1').fill(PassWrod)
      if bs.is_element_present_by_id(id='validatecode1'):
        #bs.find_by_id('captcha_field').fill(code_img)
        while True:
          val = bs.find_by_id(id='validatecode1').first.value
          if val and len(val)>0:
            bs.find_by_id('validatecode1').fill(val)
            break
          pass
        pass
      bs.find_by_name('loginSub').click()
      print 'log in'
      #bs.quit()
if __name__ == '__main__':
  log_in_doban(Name='test_account',PassWrod='test_password')
from selenium import webdriver
import time
'''
driver = webdriver.Chrome()
driver.get("http://10.10.10.28:9080/ssenewtrain/pages/frontend/login.jsp")
driver.add_cookie({'name':'username1','value':'test@sina.com'})
driver.add_cookie({'name':'password1','value':'12345678a'})
# driver.find_element_by_id("username1").send_keys("test@sina.com")
# driver.find_element_by_id("password1").send_keys("12345678a")
# driver.find_element_by_id("validatecode1").send_keys()
driver.get("http://10.10.10.28:9080/ssenewtrain/pages/frontend/login.jsp")
http://10.10.10.28:9080/ssenewtrain/verificationCode/generatedCodeForFrontend.do?timestamp=1474349106692
time.sleep(10)
driver.close()
'''