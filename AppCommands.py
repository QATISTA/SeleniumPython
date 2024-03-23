from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()














