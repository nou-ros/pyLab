'''
1. install selenium with: pip install -U selenium 
2. provide executable path for the browser
3. look for elements to find

Search for a item in google and go for specific item...
'''     
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")


driver.get("http://www.google.com")

# providing words in the google input field
driver.find_element(By.NAME, 'q').send_keys("github")
driver.implicitly_wait(10)
# selecting a specific item to search from list of items
optionList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionList))

for ele in optionList:
    print(ele.text)
    if ele.text == "github education":
        ele.click()
        break

time.sleep(5)
print(driver.title)

driver.quit()