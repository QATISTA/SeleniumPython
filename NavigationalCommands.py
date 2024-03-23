import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

driver.get("https://www.flipkart.com/")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()

driver.refresh()

driver.quit()

