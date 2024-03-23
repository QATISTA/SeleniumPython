import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# service_obj = Service("D:\TISTA\chromedriver.exe")
#
# driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")
driver.maximize_window()
driver.find_element(By.ID, "first_name").send_keys("Romit")

driver.implicitly_wait(10)
act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()
act.send_keys("romit2001@gmail.com").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("PPoo292$%qqqqq").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("Sen").perform()
driver.find_element(By.XPATH, "//*[@id='radio_1665627729_field']/ul/li[1]/label").click()
driver.find_element(By.XPATH, "//input[@id='phone_1665627880']").send_keys("9764545887")
act.send_keys(Keys.TAB).perform()
act.send_keys("9764545887").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("Indian").perform()

drp = Select(driver.find_element(By.XPATH, "//select[@id='country_1665629257']"))
drp.select_by_visible_text("Angola")
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("121").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("Test Data").perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("55").perform()
driver.find_element(By.XPATH, "//*[@id='radio_1665627931_field']/ul/li[1]/label").click()
driver.find_element(By.XPATH, "//*[@id='radio_1665627997_field']/ul/li[3]/label").click()
driver.find_element(By.XPATH, "//*[@id='radio_1665628131_field']/ul/li[2]/label").click()

drp1 = Select(driver.find_element(By.XPATH, "//select[@id='select_1665628361']"))
drp1.select_by_visible_text("Town Hall")
act.send_keys(Keys.TAB).perform()

driver.find_element(By.ID, "privacy_policy_1665633140").click()

d = driver.find_element(By.CSS_SELECTOR, "span > input.ur-flatpickr-field.regular-text")
#d.click()
dob = "1995-02-01"
driver.execute_script("arguments[0].value='" + dob + "';", d)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
