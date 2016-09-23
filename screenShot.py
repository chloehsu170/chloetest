from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    driver.find_element_by_id("kwsss").send_keys("selenium")
    driver.find_element_by_id("su").click()
    time.sleep(2)
except:
    driver.get_screenshot_as_file("C:\\Users\\user\\chloetest\\error.png")
driver.close()