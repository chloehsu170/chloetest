from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, InvalidElementStateException
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#time.sleep(0.5)
#driver.implicitly_wait(0.5)
#element = WebDriverWait(driver,2).until(lambda x:x.find_element_by_id("u1"))
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("u1"))
print(element)
#is_disappeared = WebDriverWait(driver,3,1,(InvalidElementStateException)).until_not(lambda x: x.find_element_by_id("aa").is_displayed())
is_da = WebDriverWait(driver,3,ignored_exceptions=(ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id("aa"))
#is_disappeared = WebDriverWait(driver,3,1,'ElementNotVisibleException').until_not(lambda x:x.find_element_by_id("u1").is_displayed())
print(is_da)
driver.close()