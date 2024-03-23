from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()


driver.find_element(By.XPATH, "//a[text()='nopCommerce']").click()
#driver.quit()
driver.close()