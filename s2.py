__author__ = 'chloe'
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
time.sleep(0.2)
driver = webdriver.Firefox(capabilities=caps)
time.sleep(0.2)
driver.get("http://www.gmail.com")
print(driver.title)
#driver.find_element_by_xpath(".//*[@id='gmail-sign-in']").click()
time.sleep(0.2)
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("xuyanwen170@gmail.com")
driver.find_element_by_id("next").submit()
time.sleep(1)
driver.find_element_by_id("Passwd").send_keys("c39")
driver.find_element_by_id("signIn").submit()
time.sleep(10)
driver.find_element_by_xpath(".//*[@id=':j5']/div/div[1]/span/a").click()
driver.find_element_by_xpath(".//*[@id='gb']/div[1]/div[1]/div[2]/div[4]/div[1]/a/span").click()
driver.find_element_by_id("gb_71").click()
'''
browser = webdriver.Firefox() # Get local session of firefox
#browser.get("https://www.baidu.com/") # Load page
time.sleep(0.2)
browser.get("http://www.jd.com/") # Load page
#browser.implicitly_wait(1) #wait for 1 second
#assert "京东(JD.COM)-综合网购首选-正品低价、品质保障、配送及时、轻松购物！" in browser.title
#elem = browser.find_element_by_id("kw") # Find the query box
#elem.send_keys("电动牙刷" + Keys.RETURN)
#browser.find_element_by_id("key").send_keys("电动牙刷")
#browser.find_element_by_id("search-2014").click()
#browser.find_element_by_tag_name("jr|keycount|jr_onebox|zc_buy_1").click()
time.sleep(0.2) # Let the page load, will be added to the API
if "京东(JD.COM)-综合网购首选-正品低价、品质保障、配送及时、轻松购物！" in browser.title:
    print("登录成功")
else:
    print("登录失败")
browser.find_element_by_xpath(".//*[@id='categorys-2014']/div[2]/div[1]/div[1]/h3/a").click()
time.sleep(10) # Let the page load, will be added to the API
#browser.close()
'''
