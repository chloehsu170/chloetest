from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.liaoxuefeng.com")
a = driver.get_cookies()
print(a)
driver.add_cookie({'name':'chloe','value':'170'})
for cookie in driver.get_cookies():
    print('%s -> %s' % (cookie['name'],cookie['value']))
driver.delete_cookie('chloe')
time.sleep(5)
for cookie in driver.get_cookies():
    print('%s -> %s' % (cookie['name'],cookie['value']))
time.sleep(5)
driver.delete_all_cookies()
driver.quit()