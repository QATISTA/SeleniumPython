import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# service_obj = Service("D:\TISTA\myDriver\chromedriver.exe")
# driver = webdriver.Chrome(options=options,service=service_obj)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(5)
    #Store iframe web element
iframe = driver.find_element(By.ID, "webklipper-publisher-widget-container-notification-frame")

    # switch to selected iframe
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//a[@id='webklipper-publisher-widget-container-notification-close-div']/i").click()
driver.implicitly_wait(5)
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("Hyderabad")
time.sleep(5)
driver.find_element(By.XPATH, "//span[contains(text(),'Rajiv Gandhi International Airport')]").click()
#driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']/div/div[2]").click()
driver.find_element(By.XPATH, "//input[@id='toCity']").click()
driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("Kolkata")
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Netaji Subhash Chandra Bose International Airport')]").click()

monyr = "April 2024"
day = "21"

c1 = driver.find_element(By.XPATH, "//div[@class='DayPicker-Months' ]/div[1]/div[1]/div").text
c2 = driver.find_element(By.XPATH, "//div[@class='DayPicker-Months' ]/div[2]/div[1]/div").text
if(c1 == monyr) or (c2 ==monyr):
    print("yes")
else:
    print("no")
    

