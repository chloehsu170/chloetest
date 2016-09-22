from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path ='file:///'+ os.path.abspath("drop_down.html")
driver.get(file_path)
m = driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("//option[@value='3.20']").click()
time.sleep(3)
driver.close()
