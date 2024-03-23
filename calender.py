import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")
driver.maximize_window()
time.sleep(3)
# select month and year
driver.find_element(By.XPATH,"//*[@id='date_box_1665628538_field']/span/input[1]").click()
year = "2024"
month = "January"
day = "15"

while True:
    mon = driver.find_element(By.XPATH, "//select[@aria-label='Month']").text
    yr = driver.find_element(By.XPATH, "//input[@aria-label='Year']").text

    if (mon == month) and (yr == year):

        break

    else:
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/span[2]").click()  # right arrow

#select date
d = driver.find_elements(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/span")

for x in d:
    print(x.text)
#     if (x.text == day):
#         x.click()
#         break
#
#
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
