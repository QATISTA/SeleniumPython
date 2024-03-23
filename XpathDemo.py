import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
# Absolute XPath
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/main/div/div[1]/div/article/div/div/div[3]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input").send_keys("test2")



# Relative XPath

#driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("test2")
