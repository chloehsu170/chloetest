from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('levelToLocate.html')
driver.get(file_path)
driver.implicitly_wait(2)
driver.find_element_by_link_text('Link1').click()
selement = driver.find_element_by_id('dropdown1').find_element_by_partial_link_text('Anotheraction')
ActionChains(driver).move_to_element(selement).perform()
time.sleep(2)
selement.click()
time.sleep(3)
driver.close()