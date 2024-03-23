import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select



# service_obj = Service("D:\TISTA\myDriver\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("TISTA DUTTA")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("tista.dutta@yopmail.com")
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("12345")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
driver.implicitly_wait(2)
drp = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
drp.select_by_index(1)
driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()
#driver.find_element(By.XPATH, "//input[@name='bday' and @type='date']").send_keys("05-05-2026")

d = driver.find_element(By.XPATH, "//input[@name='bday' and @type='date']")
#d.click()
d1 = "1999-02-01"
driver.execute_script("arguments[0].value='" + d1 + "';", d)

driver.find_element(By.XPATH, "//input[@value='Submit']").click()
driver.implicitly_wait(3)
msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(msg)

print("Hello World")


