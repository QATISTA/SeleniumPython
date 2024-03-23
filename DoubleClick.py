import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\myDriver\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

btn = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
time.sleep(5)
act = ActionChains(driver)

act.double_click(btn).perform()
