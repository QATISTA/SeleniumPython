import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):

        act = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, "//input[@id='user_login']").send_keys("john2265")
        act.send_keys(Keys.TAB).perform()
        act.send_keys("john20052@gmail.com")

        act.send_keys(Keys.TAB).perform()
        act.send_keys("12345&*&&DEWSjkj").perform()
        act.send_keys(Keys.TAB).perform()
        act.send_keys("12345&*&&DEWSjkj").perform()

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)
        sub = self.driver.find_element(By.XPATH, "//div[@id='ur-submit-message-node']/ul").text
        print(sub)




