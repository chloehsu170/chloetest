from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    driver.find_element_by_id("kwss").send_keys("selenium")
    driver.find_element_by_id("su").click()
except:
    driver.get_screenshot_as_file("C:\\Users\\chloe\\AppData\Local\\Programs\\Python\\Python35\chloetest\\error.png")
driver.quit()

