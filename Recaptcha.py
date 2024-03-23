import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.wpeverest.com/user-registration/recaptcha-registration-form/")
driver.maximize_window()
act = ActionChains(driver)
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("John")
act.send_keys(Keys.TAB).perform()
act.send_keys("ron1@gmail.com").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("Ron").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("Wisley").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("1234QWqw!@").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("9217652156").perform()
driver.find_element(By.XPATH, "//span[@id='recaptcha-anchor']/div[2]").click()