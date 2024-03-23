from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\SELENIUM\YT\chromedriver\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.find_element(By.NAME,'q').send_keys('abc')

# Linktext/ Partiallinktext

#driver.find_element(By.LINK_TEXT, "Register").click()

# Tag Name
links= driver.find_elements(By.TAG_NAME,'a')
print(len(links))