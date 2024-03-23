import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.redbus.com/")
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.XPATH, "//input[@id='r-date']").click()
driver.find_element(By.XPATH, "//input[@id='src']").send_keys("kolkata")









