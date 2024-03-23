from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
#text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'Tata Elxsi')]/self::a").text
#print(text_msg)


#1 parent

#txt1 = driver.find_element(By.XPATH, "//a[contains(text(), 'Tata Elxsi')]/parent::td").text
#print(txt1)

#2 child

#a = driver.find_element(By.XPATH,"//a[contains(text(),'Prestige')]").text
#print(a)


#3 ancestor
#n = driver.find_elements(By.XPATH,"//a[contains(text(),'TTK Prestige L')]/ancestor::tr/child::td")
#print(len(n))
#for x in n:
#  print(x.text)


#4 descendant
#d = driver.find_elements(By.XPATH,"//a[contains(text(),'TTK Prestige L')]/ancestor::tr/descendant::*")
#print("Number of descendant nodes = ", len(d))



#5 following
#f = driver.find_elements(By.XPATH,"//a[contains(text(),'TTK Prestige L')]/ancestor::tr/following::*")
#print("Number of following nodes = ", len(f))


#6 following-sibling
#fs = driver.find_elements(By.XPATH,"//a[contains(text(),'TTK Prestige L')]/ancestor::tr/following-sibling::*")
#print("Number of following-sibling nodes = ", len(fs))


#7 preceding
#p = driver.find_elements(By.XPATH,"//a[contains(text(),'TTK Prestige L')]/ancestor::tr/preceding::*")
#print("Number of preceding nodes = ", len(p))

#8 preceding-sibling
ps = driver.find_elements(By.XPATH,"//a[contains(text(),'TTK Prestige L')]/ancestor::tr/preceding-sibling::*")
print("Number of preceding-sibling nodes = ", len(ps))
driver.close()

