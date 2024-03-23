import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))




json_data = """
[
    {"name": "https://www.w3schools.com/html/"},
    {"name": "https://www.w3schools.com/html/html_elements.asp"},
    {"name": "https://www.w3schools.com/html/html_comments.asp"}
]
"""
# Convert JSON data to a Python object
data = json.loads(json_data)

# val = input("Enter a url: ")

wait = WebDriverWait(driver, 10)
for item in data:
    print(item["name"])
    driver.get(item["name"])
    get_url = driver.current_url
    wait.until(EC.url_to_be(item["name"]))
    if get_url == item["name"]:
        page_source = driver.page_source
    soup = BeautifulSoup(page_source, features="html.parser")
    keyword="comment"
    matches = soup.body.find_all(string=re.compile(keyword))
    len_match = len(matches)
    title = soup.title.text
    file=codecs.open('art2_txt', 'a+')
    file.write(title+"\n")
    file.write("The following are all instances of your keyword:\n")
    count=1
    for i in matches:
        file.write(str(count) + "." +  i  + "\n")
        count+=1
        file.write("There were "+str(len_match)+" matches found for the keyword.")



driver.quit()


