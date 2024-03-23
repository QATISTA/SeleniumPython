import pytest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    #service_obj = Service("D:\TISTA\myDriver\chromedriver.exe")
    #driver = webdriver.Chrome(service=service_obj)
    driver.get("https://demo.wpeverest.com/user-registration/rounded-edge/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

