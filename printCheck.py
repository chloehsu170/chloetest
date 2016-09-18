from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(1)
title = driver.title
print(title)
if title == "百度一下，你就知道":
    print("title is correct!")
else:
    print("title is wrong!")

url =driver.current_url
print(url)
if url =="https://www.baidu.com/":
    print("correct url")
else:
    print("wrong url")
time.sleep(3)
driver.close()