from selenium import webdriver
import time
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

driver = webdriver.Firefox(capabilities=caps)
time.sleep(2)'''
driver =webdriver.Edge()
driver.get("http://www.baidu.com")
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='u1']/a[8]").click()
time.sleep(1)
driver.find_element_by_link_text("搜索设置").click()
#driver.find_element_by_xpath(".//*[@id='wrapper']/div[5]/a[1]")
time.sleep(2)

driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
time.sleep(2)
alert = driver.switch_to_alert()
alert.accept()
print(alert.text)
time.sleep(2)
driver.close()

