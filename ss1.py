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
time.sleep(3)
browser.find_element_by_xpath("html/body/div[2]/div/div[2]/div[1]/div[2]/div/div[6]/table/tbody/tr/td[1]/span").click()
browser.find_element_by_xpath(".//*[@id='datagrid-row-r1-2-49']/td[2]/div").send_keys("8")
time.sleep(3)
browser.quit()
html/body/div[2]/div/div[2]/div[1]/div[2]/div/div[5]/table/tbody/tr/td[1]/span