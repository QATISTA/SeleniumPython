from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed  is_enabled
searchbox= driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status: ",searchbox.is_displayed())
print("Enabled status: ",searchbox.is_enabled())

# is_selected
selM = driver.find_element(By.XPATH, "//input[@value='M']").is_selected()
print("Selected status Male: ", selM)

selF = driver.find_element(By.XPATH, "//input[@value='F']").is_selected()
print("Selected status Female: ", selF)

driver.quit()



