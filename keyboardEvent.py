from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
wbk = driver.find_element_by_id("kw")
wbk.send_keys("xuyanwen")
wbk.send_keys(Keys.BACK_SPACE)
wbk.send_keys(Keys.SPACE + "170")
wbk.send_keys(Keys.CONTROL,'a') #quanxuan
a = wbk.get_attribute('value')
print(a)
time.sleep(3)
wbk.send_keys(Keys.CONTROL,'x') #jiantie
time.sleep(3)
wbk.send_keys(Keys.CONTROL,'v'+Keys.ENTER) #zhatie
#wbk.send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
