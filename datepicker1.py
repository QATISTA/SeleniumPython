import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # switch to frame
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

# select month and year
year = "2024"
month = "July"
day = "1"

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if (mon == month) and (yr == year):
        break

    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # right arrow

# select date
d = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for x in d:
    if (x.text == day):
        x.click()
        break





