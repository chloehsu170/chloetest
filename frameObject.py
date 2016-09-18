from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('frame.html')
driver.get(file_path)
driver.switch_to_frame("f1")
driver.switch_to_frame("f2")
driver.find_element_by_id("kw").send_keys('selenium'+Keys.RETURN)
time.sleep(3)
#driver.close()


