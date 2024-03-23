import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com/account/login")
driver.maximize_window()
x = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
x.send_keys("abc@gmail.com")
print("For text: ", x.text)
print("For get_attribute: ", x.get_attribute('value'))































