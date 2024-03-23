import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
# service_obj = Service("D:\TISTA\myDriver\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.spicejet.com/")
driver.maximize_window()
driver.implicitly_wait(10)

print("hii world")
