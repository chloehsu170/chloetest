from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path ='file:///'+os.path.abspath("page.html")
driver.get(file_path)
driver.implicitly_wait(5)
m = len(driver.find_element_by_tag_name("select").find_elements_by_tag_name("option"))
print("total pages is %s"% m)
pages = driver.find_element_by_tag_name("select").find_elements_by_tag_name("option")
for page in pages:
    page.click()
    time.sleep(2)
driver.close()