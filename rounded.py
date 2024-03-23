import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:\TISTA\myDriver\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.wpeverest.com/user-registration/rounded-edge/")
driver.maximize_window()
act = ActionChains(driver)
driver.find_element(By.XPATH, "//input[@id='user_login']").send_keys("john2265")
act.send_keys(Keys.TAB).perform()
act.send_keys("john10052@gmail.com")

act.send_keys(Keys.TAB).perform()
act.send_keys("12345&*&&DEWSjkj").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("12345&*&&DEWSjkj").perform()

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(4)
sub = driver.find_element(By.XPATH, "//div[@id='ur-submit-message-node']/ul").text
print(sub)

