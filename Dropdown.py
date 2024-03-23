from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# service_obj = Service("D:\TISTA\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
driver.maximize_window()


drp = Select(driver.find_element(By.XPATH, "//select[@id='first']"))

drp.select_by_visible_text("Google")
# drp.select_by_index(2)
# drp.select_by_value("1")

# capture all the options and print them

# Approach 1
# a = driver.find_elements(By.XPATH, "//select[@id='first']/child::option")
# for item in a:
#     print(item.text)

# Approach 2
# drp = Select(driver.find_element(By.XPATH, "//select[@id='first']"))
# n = drp.options
#
# for num in n:
#     print(num.text)