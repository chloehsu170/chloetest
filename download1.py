from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities.FIREFOX
import os
from selenium import webdriver
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", 'C:\\Users\\chloe')
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
"application/octet-stream")
browser = webdriver.Firefox(firefox_profile=fp,capabilities=caps,)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-3.0.0b3.tar.gz").click()