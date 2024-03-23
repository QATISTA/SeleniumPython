import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

alartWindow = driver.switch_to.alert
print(alartWindow.text)
alartWindow.send_keys("India")
# alartWindow.accept()

alartWindow.dismiss()




