__author__ = 'chloe'
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

'''
from selenium import webdriver
driver = webdriver.Ie()
first_url ="http://www.baidu.com"
print('now access to:%s' % first_url)
driver.get(first_url)
second_url ="http://news.baidu.com"
print('now access to:%s' % second_url)
driver.get(second_url)
print('now back to:%s' % first_url)
driver.back()
print('now back to:%s' % second_url)
driver.forward()
'''
driver = webdriver.Chrome()
time.sleep(0.2)
driver.get("https://www.baidu.com")
print(driver.title)
#driver.find_element_by_xpath(".//*[@id='gmail-sign-in']").click()
time.sleep(0.2)
text = driver.find_element_by_id("jgwab").text#beianxinxi
print(text)
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click() #denglu
time.sleep(2)
size = driver.find_element_by_id("TANGRAM__PSP_8__userName").size #yonghumingkuanggaodu
print(size)
driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("徐燕雯")
attribute = driver.find_element_by_id("TANGRAM__PSP_8__userName").get_attribute('type')
result = driver.find_element_by_id("TANGRAM__PSP_8__userName").is_displayed()
print(result)
print(attribute)
time.sleep(1)



#print(driver.title)

#driver.set_window_size(800,480)

#driver.quit()

