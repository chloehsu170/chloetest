from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://www.baidu.com")

map = driver.find_element_by_xpath(".//*[@id='u1']/a[4]")
#ActionChains(driver).move_to_element(map).perform() #移动到元素上
ActionChains(driver).click_and_hold(map).perform() #执行左键并按下
time.sleep(1)
title = driver.title
print(title)
'''
#place = driver.find_element_by_xpath("//div[@id='platform']/canvas")
place = driver.find_element_by_xpath("//canvas")
ActionChains(driver).double_click(place).perform()
ActionChains(driver).double_click(place).perform()
time.sleep(3)
driver.close()
'''