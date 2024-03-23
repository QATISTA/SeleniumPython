import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# select all the checkboxes

# Approach1
'''c = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
print(len(c))
for check in c:
    check.click()'''


# Approach2
'''c = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
checkb = len(c)

for i in range(checkb):
    c[i].click()'''


# select multiple checkboxes by choice (Thursday and Sunday)

c = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")

for check in c:
    if check.get_attribute('value') == 'thursday' or check.get_attribute('value') == 'sunday':
        check.click()
















