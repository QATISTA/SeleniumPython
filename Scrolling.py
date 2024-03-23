import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://geographyfieldwork.com/WorldCapitalCities.htm")
driver.maximize_window()
time.sleep(3)

#1 Scroll down page by Pixel
# driver.execute_script("window.scrollBy(0,2500)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved: ", value)


#2 Scroll down till the element is visible
# c = driver.find_element(By.CSS_SELECTOR, "#anyid > tbody > tr:nth-child(174) > td:nth-child(1)")
# driver.execute_script("arguments[0].scrollIntoView();", c)


# Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# Scroll up to the starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")