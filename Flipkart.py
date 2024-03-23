import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//span[@role='button']").click()
driver.find_element(By.XPATH,"//input[@name='q']").send_keys("iphone 15 pro max")
driver.find_element(By.XPATH, "//button[@title='Search for Products, Brands and More']").click()
driver.find_element(By.XPATH, "//div[text()='APPLE iPhone 15 Pro Max (Black Titanium, 256 GB)']").click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
time.sleep(5)

driver.find_element(By.XPATH, "//button[text()='Buy Now']").click()









