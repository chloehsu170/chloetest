import userInfo
from selenium import  webdriver
infos =userInfo.zidian()
for info in infos:
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(info)
    driver.find_element_by_id("su").click()
    driver.quit()
