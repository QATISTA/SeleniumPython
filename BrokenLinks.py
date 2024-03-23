# we need to install requests package through File > Settings > Project Interpreter > +


import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,"a")

count = 0
for l in links:
    url = l.get_attribute('href')

    try:
        r = requests.head(url)
    except:
        None
    if r.status_code >= 400 :
        print(url, "is broken")
        count+= 1
    else:
        print(url, "is valid")
print("Total number of broken links are: ", count)
print("Total links available: ", len(links))
valid_links = len(links)- count
print("Total number of valid links are: ", valid_links)