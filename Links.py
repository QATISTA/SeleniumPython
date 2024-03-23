import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
# driver.find_element(By.LINK_TEXT, "Computers").click()


# find total no. of links

total = driver.find_elements(By.TAG_NAME, "a")
print(len(total))

# print all the link name
for t in total:
    print(t.text)









