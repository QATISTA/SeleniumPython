import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='dob']").click()










