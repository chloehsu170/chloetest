from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('setOfObjectHtml.html')
driver.get(file_path)
driver.implicitly_wait(2)
checkboxex = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxex:
    checkbox.click()
print(len(checkboxex))
time.sleep(2)
checkboxex.pop().click()