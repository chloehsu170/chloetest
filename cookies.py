from selenium import webdriver
import os,time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.add_cookie({'name':'xuyanwen','value':'haha'})
cookie = driver.get_cookie('xuyanwen')
cookie = driver.get_cookie('haha')
for cookie in driver.get_cookies():
   print("%s -> %s"% (cookie['name'],cookie['value']))

driver.quit()
