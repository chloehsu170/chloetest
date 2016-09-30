from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

driver = webdriver.Firefox(capabilities=caps)
time.sleep(2)
#driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(2)

currentWindow = driver.current_window_handle
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__submitWrapper']/a[1]").click()
allWindows = driver.window_handles
for window in allWindows:
    if window != currentWindow:
        print("you are access to register window!")
        driver.switch_to_window(window)
        time.sleep(2)
        print(driver.title)
time.sleep(2)
print(len(allWindows))
driver.switch_to_window(currentWindow)
print(driver.title)
driver.find_element_by_name('userName').send_keys('selium')
time.sleep(3)
#driver.close()

