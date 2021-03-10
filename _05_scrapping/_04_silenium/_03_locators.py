'''
By.ID -	driver.find_element(By.ID (<element ID>)) - Locates an element using the ID attribute
By.NAME	- driver.find_element(By.NAME (<element name>)) - Locates an element using the Name attribute
By class name - driver.find_element(By.className (<element class>)) - Locates an element using the Class attribute
By tag name	- driver.find_element(By.tagName (<htmltagname>)) - Locates an element using the HTML tag
By.LINK_TEXT - driver.find_element(By.LINK_TEXT (<linktext>)) - Locates a link using link text
By partial link text - driver.find_element(By.partialLinkText (<linktext>) - Locates a link using the link's partial text
By CSS - driver.find_element(By.cssSelector (<css selector>)) - Locates an element using the CSS selector
By XPath - driver.find_element(By.xpath (<xpath>)) - Locates an element using XPath query
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

# By.ID
username = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
# selecting a link By.LINK_TEXT
feature_link = driver.find_element(By.LINK_TEXT, 'Features')

username.send_keys('nouros test')
first_name.send_keys('nouros')
last_name.send_keys('test')
email.send_keys('test@testmail.com')

feature_link.click()



driver.get("https://classic.crmpro.com/")
print(driver.title)

#By.NAME
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

#By.XPATH as there are no ID or NAME
#for searching XPATH type ctrl+f in the dev tools and look using //input[@value='Login']
login = driver.find_element(By.XPATH, "//input[@value='Login']")

username.send_keys('batchautomation')
password.send_keys('Test@12345')
login.click()