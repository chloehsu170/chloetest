from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('getAttribute.html')
driver.get(file_path)
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute("data-node") == '594434493':
        input.click()
time.sleep(3)
driver.quit()
