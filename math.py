from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("xuyanwen")
a = driver.find_element_by_id("kw").get_attribute("id")
b = driver.find_element_by_id("kw").is_displayed()
c = driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
d = driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
e = driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
is_disappeared = Web
print(a)
print(c)
driver.quit()