import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.maximize_window()

