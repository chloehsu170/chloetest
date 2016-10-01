from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("电动牙刷")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='con-ar']/div[1]/div/div/div[4]/div/div[1]/div[2]/a").click()
time.sleep(3)
driver.close()