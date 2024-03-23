import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail%2Blogin%26oq%3Dgmail%2B%26gs_lcrp%3DEgZjaHJvbWUqFAgAEEUYOxhDGIMBGLEDGIAEGIoFMhQIABBFGDsYQxiDARixAxiABBiKBTIGCAEQRRg5Mg0IAhAAGIMBGLEDGIAEMg0IAxAAGIMBGLEDGIAEMgoIBBAAGLEDGIAEMgYIBRBFGD0yBggGEEUYPDIGCAcQRRg8qAIAsAIA%26pf%3Dcs%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAZAAQ&hl=en&ifkv=ASKXGp0Rng9jxrniVtIAtzQ76OZxZ6BShmRAkaMB1R__PxA93XM1PGpVqNLAD8iGAz7UNTeGRyBG7Q&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1342542908%3A1700561909437949&theme=glif")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("chesslovertista@gmail.com")
driver.find_element(By.XPATH, "//span[text()='Next']").click()