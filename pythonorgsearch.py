__author__ = 'chloe'
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python.org" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon123")
elem.send_keys(Keys.RETURN)
assert "No results found." in driver.page_source
driver.close()
