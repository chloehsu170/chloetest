from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
caps=DesiredCapabilities.FIREFOX
caps["marionette"]=True
caps["binary"] ="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
fp = webdriver.FirefoxProfile()
fp.set_preference("brower.download.folderlist",1)
fp.set_preference("brower.download.manager.showWhenStaring",False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/x-gzip")
browser = webdriver.Firefox(firefox_profile=fp,capabilities=caps)
browser.implicitly_wait(5)
browser.get("http://apache.fayea.com/maven/maven-3/3.3.9/binaries/")
browser.implicitly_wait(5)
browser.find_element_by_link_text("apache-maven-3.3.9-bin.tar.gz").click()