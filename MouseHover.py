from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
# MouseHover
inter = driver.find_element(By.XPATH, "//a[@data-toggle='dropdown' and @href='Interactions.html']")
dnd = driver.find_element(By.XPATH, "//a[text()='Drag and Drop ']")
dynamic = driver.find_element(By.XPATH, "//a[@href='Dynamic.html']")

act = ActionChains(driver)
act.move_to_element(inter).move_to_element(dnd).move_to_element(dynamic).click().perform()



