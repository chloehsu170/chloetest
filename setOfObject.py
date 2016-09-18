#file:///C:/Users/chloe/Documents/Tencent%20Files/646567397/FileRecv/selenium2python自动化测试实战修订.pdf
import time
from selenium import webdriver
import os

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath("setOfObjectHtml.html")
driver.get(file_path)
inputs = driver.find_elements_by_tag_name('input')
'''
for input in inputs:
    if input.get_attribute('type') =='checkbox':
        input.click()
        '''
for input in inputs:
    if input.get_attribute('id')=='c2'or 'c3':
        input.click()
time.sleep(3)
driver.close()
#file_path = 'file:///'+os.path.abspath("setOfObjectHtml.html")