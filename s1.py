__author__ = 'chloe'
#coding=utf-8
#import selenium print selenium.__file__
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://10.10.10.46:8080/sse-spm/sys/user/logout.html")
browser.implicitly_wait(10)
browser.find_element_by_id("userName").send_keys("xuyanwen")
browser.find_element_by_id("password").send_keys("pass")
browser.find_element_by_id("LoginBtn").click()
browser.implicitly_wait(10)
browser.find_element_by_xpath(".//*[@id='signstar_wrapper']/a[1]").click()
browser.quit()
