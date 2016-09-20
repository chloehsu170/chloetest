from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///'+ os.path.abspath("upload.html")
driver.get(file_path)
driver.find_element_by_name("file").send_keys("C:\\Users\\chloe\\Desktop\\geckodriver.log")
time.sleep(3)
driver.close()
