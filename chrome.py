__author__ = 'chloe'
# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
# This will not be necessary in the future,
# when Selenium will auto-detect what remote end
# it is talking to.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
# Firefox 47 (stable) is currently not supported,
# and may give you a suboptimal experience.
#
# On Mac OS you must point to the binary executable
# inside the application package, such as
# /Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin
#caps["binary"] = "/usr/bin/firefox"
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
#C:\Program Files (x86)\Mozilla Firefox\firefox.exe
driver = webdriver.Firefox(capabilities=caps)
#driver = webdriver.Firefox()
#time.sleep(0.1) #等待页面刷新
driver.get('http://www.baidu.com')

print(driver.title)

driver.quit()

