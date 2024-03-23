import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.globalsqa.com/demoSite/practice/slider/range.html")
driver.maximize_window()
time.sleep(3)

act = ActionChains(driver)
min_range = driver.find_element(By.CSS_SELECTOR, "#slider-range > span:nth-child(2)")
max_range = driver.find_element(By.CSS_SELECTOR, "#slider-range > span:nth-child(3)")
a = min_range.location
b = max_range.location
print("Min Location before sliding", a) # {'x': 202, 'y': 46}
print("Max Location before sliding", b) # {'x': 808, 'y': 46}

act.drag_and_drop_by_offset(min_range,100,0).perform()
act.drag_and_drop_by_offset(max_range,-55,0).perform()

x = min_range.location
y = max_range.location
print("Min Location after sliding", x)  # {'x': 301, 'y': 46}
print("Max Location after sliding", y) # {'x': 754, 'y': 46}