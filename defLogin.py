def login(self):
    driver = self.driver
    driver.find_element_by_id("kw").send_keys("selenium webdriver")
    driver.find_element_by_id("su").click()