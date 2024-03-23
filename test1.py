# 1) Open Web Browser
# 2) Open URL https://poswebsol.sticky.io/
# 3) Enter Username (IMC-DEV)
# 4) Enter Password  (lG8i0#2g@##)
# 5) Click on Login.
# 6) Capture title of home page. (Actual Title)
# 7) Verify title of the page: ..  (Expected)
# 8) Close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\SELENIUM\YT\chromedriver\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://poswebsol.sticky.io/")
driver.find_element(By.NAME, "admin_name" ).send_keys("IMC-DEV")
driver.find_element(By.NAME, "admin_pass" ).send_keys("lG8i0#2g@##")
driver.find_element(By.XPATH, "//button[@type='submit']" ).click()

while('true'):

    pass




