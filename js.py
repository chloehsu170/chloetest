from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("js.html")
driver.get(file_path)
tooltip = driver.find_element_by_id("tooltip")
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)
is_appeared =tooltip.is_displayed()
print(is_appeared)
button =driver.find_element_by_class_name("btn")
driver.execute_script('$(arguments[0]).fadeOut()',button)
time.sleep(5)
is_appeared1 = button.is_displayed()
print(is_appeared1)
driver.quit()