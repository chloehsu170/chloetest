from selenium import webdriver
import os,time

data = open('C:\\Users\\user\\chloetest\\baiduReadData.txt','r')
source =data.readlines()
data.close()
for s in source:
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(s)
    driver.find_element_by_id("su").click()
    time.sleep(3)
    driver.close()