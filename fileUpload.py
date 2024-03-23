import time

from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.wpeverest.com/user-registration/file-upload-form/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='user_email']").send_keys("ron1@gmail.com")
driver.find_element(By.XPATH, "//input[@name='user_pass']").send_keys("QWERqwer1234!@")
driver.find_element(By.CSS_SELECTOR, "#ur_file_1641275829 > div > span.user-registration-file-upload-title").click()
time.sleep(3)


keyboard = Controller()
keyboard.type("D:\\TISTA\\abc.pdf")
keyboard.press(Key.enter)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
x = driver.find_element(By.XPATH, "//*[@id='ur-submit-message-node']/ul").text

print(x)

